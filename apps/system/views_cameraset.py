# @Time   : 2018/10/18 23:04
# @Author : RobbieHan
# @File   : views_cameraset.py

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
from .models import CameraSet,Structure
from .forms import CameraSetForm
from apps.custom import BreadcrumbMixin
from django.conf import settings
from django.db.models import Q
from .tasks import test
User = get_user_model()


class CameraSetView(LoginRequiredMixin,  BreadcrumbMixin, TemplateView):

    template_name = 'system/cameraset/cameraset.html'


class CameraSetCreateView(LoginRequiredMixin, View):

    def get(self, request):
        role = request.user.roles.first().name  # 能登录的人都有角色
        if role == '系统管理员':
            ret = dict(company_all=Structure.objects.filter(level=0))
        elif role == '公司级管理员':
            ret = dict(company_all=Structure.objects.filter(tree_id=request.user.department.tree_id,level=0))

        if 'id' in request.GET and request.GET['id']:
            cameraset = get_object_or_404(CameraSet, pk=request.GET['id'])
            ret['cameraset'] = cameraset
            ret['role'] = role
        return render(request, 'system/cameraset/cameraset_create.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            cameraset = get_object_or_404(CameraSet, pk=request.POST['id'])
        else:
            cameraset = CameraSet()
        cameraset_form = CameraSetForm(request.POST, instance=cameraset)
        if cameraset_form.is_valid():
            cameraset = cameraset_form.save()
            test.delay(cameraset.id)
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class CameraSetListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'usercam', 'pwdcam','ipcam','portcam', 'webcamid','company__name']

        role = request.user.roles.first().name  # 能登录的人都有角色
        if role == '系统管理员':
            ret = dict(data=list(CameraSet.objects.values(*fields)))
        elif role == '公司级管理员':
            ret = dict(data=list(CameraSet.objects.filter(company__tree_id=request.user.department.tree_id).values(*fields)))


        return HttpResponse(json.dumps(ret), content_type='application/json')


class CameraSetDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST['id'].split(','))
            CameraSet.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


