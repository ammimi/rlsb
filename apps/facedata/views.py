import json
import re

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import FaceData
from .forms import FaceDataCreateForm,FaceDataUpdateForm
from system.models import Menu,SystemSetup
from system.mixin import LoginRequiredMixin

# Create your views here.

class FaceDataView(LoginRequiredMixin, View):

    def get(self, request):
        ret = Menu.get_menu_by_request_url(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        ret['titles'] = ('姓名','人脸样本ID','人脸拼音名称','人脸中文名称','人脸样本图片Url地址','详情')
        return render(request, 'oa/facedata/facedata.html', ret)


class FaceDataListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'owner__name', 'face_id', 'face_name','face_cname', 'face_image_url',]
        filters = dict()
        #部门过滤条件
        # if request.user.department_id == 9:
        #     filters['belongs_to_id'] = request.user.id
        ret = dict(data=list(FaceData.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class FaceDataCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()

        ret['form'] = FaceDataCreateForm(user=request.user)
        # ret['user_info'] = user_info

        return render(request, 'oa/facedata/facedata_create.html', ret)

    def post(self, request):
        res = dict()
        facedata_create_form = FaceDataCreateForm(request.POST,user=request.user)
        if facedata_create_form.is_valid():
            facedata_create_form.save()
            res['status'] = 'success'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(facedata_create_form.errors)
            facedata_create_form = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'facedata_create_form': facedata_create_form[0]
            }

        return HttpResponse(json.dumps(res), content_type='application/json')


class FaceDataUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        status_list = []
        if 'id' in request.GET and request.GET['id']:
            facedata = get_object_or_404(FaceData, pk=request.GET['id'])
            ret['facedata'] = facedata
            ret['form'] = FaceDataUpdateForm(instance=facedata,user=request.user)

        return render(request, 'oa/facedata/facedata_update.html', ret)

    def post(self, request):
        res = dict()
        facedata = get_object_or_404(FaceData, pk=request.POST['id'])
        facedata_update_form = FaceDataUpdateForm(request.POST, instance=facedata,user=request.user)
        if facedata_update_form.is_valid():
            facedata_update_form.save()
            res['status'] = 'success'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(facedata_update_form.errors)
            facedata_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'Acl_form_errors': facedata_form_errors[0]
            }

        return HttpResponse(json.dumps(res), content_type='application/json')

class FaceDataDetailView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            facedata = get_object_or_404(FaceData, pk=request.GET.get('id'))
            ret['facedata'] = facedata
            # ret['Acl_log'] = Acl_log
        return render(request, 'oa/facedata/facedata_detail.html', ret)


class FaceDataDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            FaceData.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')