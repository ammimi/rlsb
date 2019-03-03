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
from system.forms import UserCreateForm,UserUpdateForm
from system.models import Menu,SystemSetup,Structure
from system.mixin import LoginRequiredMixin
from .forms import FaceDataForm

# Create your views here.

class FaceDataView(LoginRequiredMixin, View):

    def get(self, request):

        role = request.user.roles.first().name
        if role == '系统管理员':
            nodes = Structure.objects.all()
        elif role == '公司级管理员':
            nodes = Structure.objects.filter(tree_id=request.user.department.tree_id)
        elif role == '部门管理员':  # 最多支持3级
            nodes = Structure.objects.filter(
                Q(tree_id=request.user.department.tree_id, level=1, id=request.user.department.id) |  # 一级
                Q(tree_id=request.user.department.tree_id, level=2, parent__id=request.user.department.id) |  # 二级
                Q(tree_id=request.user.department.tree_id, level=3, parent__parent__id=request.user.department.id)  # 三级
                )

        ret = Menu.get_menu_by_request_url(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        ret['nodes'] = nodes
        ret['titles'] = ('姓名','部门','人脸样本ID','人脸拼音名称','人脸中文名称','人脸样本图片','是否同步人脸数据','详情')
        ret['form'] =  FaceDataForm()
        return render(request, 'oa/facedata/facedata.html', ret)


class FaceDataListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'name', 'department__name','face_id', 'face_name','face_cname', 'face_image','ifsync']
        filters = dict()
        if 'name' in request.GET and request.GET['name']:
            filters['name'] = request.GET['name']
        if 'department' in request.GET and request.GET['department']:
            filters['department__id'] = request.GET['department']
        print (filters)

        ret = dict(data=list(FaceData.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class FaceDataCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()


        role = request.user.roles.first().name  # 能登录的人都有角色
        if role == '系统管理员':
            ret = dict(structure_all=Structure.objects.all())
        elif role == '公司级管理员':
            ret = dict(structure_all=Structure.objects.filter(tree_id=request.user.department.tree_id))
        ret['form'] = FaceDataCreateForm(user=request.user)
        return render(request, 'oa/facedata/facedata_create.html', ret)

    def post(self, request):
        res = dict()
        facedata_create_form = FaceDataCreateForm(request.POST,request.FILES or None,user=request.user)
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
        facedata_update_form = FaceDataUpdateForm(request.POST,request.FILES or None, instance=facedata,user=request.user)
        if facedata_update_form.is_valid():
            facedata_update_form.save()
            res['status'] = 'success'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(facedata_update_form.errors)
            facedata_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'facedata_update_form': facedata_form_errors[0]
            }

        return HttpResponse(json.dumps(res), content_type='application/json')

class FaceDataDetailView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            facedata = get_object_or_404(FaceData, pk=request.GET.get('id'))
            ret['facedata'] = facedata
        return render(request, 'oa/facedata/facedata_detail.html', ret)


class FaceDataDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            FaceData.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')