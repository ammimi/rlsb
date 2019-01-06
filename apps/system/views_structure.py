# @Time   : 2018/10/18 23:04
# @Author : RobbieHan
# @File   : views_structure.py

import hashlib
import time
import json
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .mixin import LoginRequiredMixin
from .models import Structure
from .forms import StructureForm
from apps.custom import BreadcrumbMixin
from django.conf import settings

from apps.utils.sendClientDataOnClientTest import sendClientData
from apps.utils.deleteClientDataOnClientTest import deletClientData
from apps.utils.updateClientDataOnClientTest import updateClientData

User = get_user_model()


class StructureView(LoginRequiredMixin,  BreadcrumbMixin, TemplateView):

    template_name = 'system/structure/structure.html'


class StructureCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict(structure_all=Structure.objects.all())
        if 'id' in request.GET and request.GET['id']:
            structure = get_object_or_404(Structure, pk=request.GET['id'])
            ret['structure'] = structure
        return render(request, 'system/structure/structure_create.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            structure = get_object_or_404(Structure, pk=request.POST['id'])
        else:
            structure = Structure()
        structure_form = StructureForm(request.POST, instance=structure)
        if structure_form.is_valid():
            structure_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class StructureListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'name', 'type','client_id','client_secret', 'parent__name']
        ret = dict(data=list(Structure.objects.values(*fields)))
        return HttpResponse(json.dumps(ret), content_type='application/json')


class StructureDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST['id'].split(','))
            Structure.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class Structure2UserView(LoginRequiredMixin, View):

    def get(self, request):
        if 'id' in request.GET and request.GET['id']:
            structure = get_object_or_404(Structure, pk=int(request.GET['id']))
            added_users = structure.userprofile_set.all()
            all_users = User.objects.all()
            un_add_users = set(all_users).difference(added_users)
            ret = dict(structure=structure, added_users=added_users, un_add_users=list(un_add_users))
        return render(request, 'system/structure/structure_user.html', ret)

    def post(self, request):
        res = dict(result=False)
        id_list = None
        structure = get_object_or_404(Structure, pk=int(request.POST['id']))
        if 'to' in request.POST and request.POST.getlist('to', []):
            id_list = map(int, request.POST.getlist('to', []))
        structure.userprofile_set.clear()
        if id_list:
            for user in User.objects.filter(id__in=id_list):
                structure.userprofile_set.add(user)
        res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class AddClientView(LoginRequiredMixin, View):
    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            structure = get_object_or_404(Structure, pk=request.POST.get('id'))

            clientSecret = structure.client_secret
            clientName = structure.client_name
            clientCName = structure.client_name

            timestamp = int(time.time())
            url = settings.RLSBURL+"clientmng/addClient"

            params = {"client_secret": clientSecret, "client_name": clientName, "client_cname": clientCName,
                      "timestamp": timestamp}

            paramNamesForSignature = sorted(["client_secret", "client_name", "timestamp"], key=str.lower)

            paramValuesStr = ""
            for index in range(0, len(paramNamesForSignature)):
                param = paramNamesForSignature[index]
                paramValuesStr += str(params[param])

            m = hashlib.md5()
            m.update(paramValuesStr.encode("utf-8"))
            signatureStr = m.hexdigest()

            params["signature"] = signatureStr

            send_client_data = sendClientData(url, params)

            res = dict()
            if send_client_data['result'] =='success':
                res['status'] = 'success'
                structure.client_id = send_client_data['client_id']
                structure.save()
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = send_client_data['error_msg']

                res = {
                    'status': 'fail',
                    'send_client_data': errors
                }

        return HttpResponse(json.dumps(res), content_type='application/json')

class DeleteClientView(LoginRequiredMixin, View):
    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            structure = get_object_or_404(Structure, pk=request.POST.get('id'))

            clientId = structure.client_id
            clientSecret = structure.client_secret


            timestamp = int(time.time())
            url = settings.RLSBURL+"clientmng/deleteClient"

            params = {"client_id": clientId, "client_secret": clientSecret, "timestamp": timestamp}

            paramNamesForSignature = sorted(["client_secret", "client_id", "timestamp"], key=str.lower)

            paramValuesStr = ""
            for index in range(0, len(paramNamesForSignature)):
                param = paramNamesForSignature[index]
                paramValuesStr += str(params[param])

            m = hashlib.md5()
            m.update(paramValuesStr.encode("utf-8"))
            signatureStr = m.hexdigest()

            params["signature"] = signatureStr

            delete_client_data = deletClientData(url, params)

            res = dict()
            if delete_client_data['result'] =='success':
                res['status'] = 'success'
                structure.client_id = None
                structure.save()
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = delete_client_data['error_msg']

                res = {
                    'status': 'fail',
                    'delete_client_data': errors
                }

        return HttpResponse(json.dumps(res), content_type='application/json')

class UpdateClientView(LoginRequiredMixin, View):
    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            structure = get_object_or_404(Structure, pk=request.POST.get('id'))

            clientId = structure.client_id
            clientSecret = structure.client_secret

            clientName = structure.client_name
            clientCName = structure.client_cname


            timestamp = int(time.time())
            url = settings.RLSBURL+"clientmng/updateClient"

            params = {"client_id": clientId, "client_secret": clientSecret, "client_name": clientName,
                      "client_cname": clientCName, "timestamp": timestamp}

            paramNamesForSignature = sorted(["client_secret", "client_name", "client_id", "timestamp"], key=str.lower)

            paramValuesStr = ""
            for index in range(0, len(paramNamesForSignature)):
                param = paramNamesForSignature[index]
                paramValuesStr += str(params[param])

            m = hashlib.md5()
            m.update(paramValuesStr.encode("utf-8"))
            signatureStr = m.hexdigest()

            params["signature"] = signatureStr

            updata_client_data = updateClientData(url, params)

            res = dict()
            if updata_client_data['result'] =='success':
                res['status'] = 'success'

            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = updata_client_data['error_msg']

                res = {
                    'status': 'fail',
                    'updata_client_data': errors
                }

        return HttpResponse(json.dumps(res), content_type='application/json')

class GetClientIDInfo:

    def __init__(self,userid):
        self.user = get_object_or_404(User, pk=userid)

    def get_parent(self):
        department = self.user.department
        if department:
            if department.parent :
                parent = department.parent
            else:
                parent = department

            return parent

    def get_clientid(self):
        return self.get_parent().client_id

    def get_clientsecret(self):
        return self.get_parent().client_secret
