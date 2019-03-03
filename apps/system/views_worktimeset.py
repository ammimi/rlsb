# @Time   : 2018/10/18 23:04
# @Author : RobbieHan
# @File   : views_worktimeset.py

import hashlib
import time
import json
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder

from .mixin import LoginRequiredMixin
from .models import WorktimeSet,Structure
from .forms import WorktimeSetForm
from apps.custom import BreadcrumbMixin
from django.conf import settings
from django.db.models import Q

User = get_user_model()


class WorktimeSetView(LoginRequiredMixin,  BreadcrumbMixin, TemplateView):

    template_name = 'system/worktimeset/worktimeset.html'


class WorktimeSetCreateView(LoginRequiredMixin, View):

    def get(self, request):
        role = request.user.roles.first().name  # 能登录的人都有角色
        if role == '系统管理员':
            ret = dict(company_all=Structure.objects.filter(level=0))
        elif role == '公司级管理员':
            ret = dict(company_all=Structure.objects.filter(tree_id=request.user.department.tree_id,level=0))

        if 'id' in request.GET and request.GET['id']:
            worktimeset = get_object_or_404(WorktimeSet, pk=request.GET['id'])
            ret['worktimeset'] = worktimeset
            ret['role'] = role
        return render(request, 'system/worktimeset/worktimeset_create.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            worktimeset = get_object_or_404(WorktimeSet, pk=request.POST['id'])
        else:
            worktimeset = WorktimeSet()
        worktimeset_form = WorktimeSetForm(request.POST, instance=worktimeset)
        if worktimeset_form.is_valid():
            worktimeset_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class WorktimeSetListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'uptime', 'downtime','company__name']

        role = request.user.roles.first().name  # 能登录的人都有角色
        if role == '系统管理员':
            ret = dict(data=list(WorktimeSet.objects.values(*fields)))
        elif role == '公司级管理员':
            ret = dict(data=list(WorktimeSet.objects.filter(company__tree_id=request.user.department.tree_id).values(*fields)))

        return HttpResponse(json.dumps(ret,cls=DjangoJSONEncoder), content_type='application/json')


class WorktimeSetDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST['id'].split(','))
            WorktimeSet.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


