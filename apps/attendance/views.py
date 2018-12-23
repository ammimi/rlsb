import json
import re

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.db.models import Q


from system.mixin import LoginRequiredMixin
from .models import AttendanceInfo
from .forms import AttendanceInfoForm,AttendanceInfoCreateForm,AttendanceInfoUpdateForm
from system.models import Role,Menu
from system.models import SystemSetup



User = get_user_model()


class AttendanceInfoView(LoginRequiredMixin, View):

    def get(self, request):
        ret = Menu.get_menu_by_request_url(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        ret['titles'] = ('姓名','考勤时间','考勤图片','详情')
        return render(request, 'oa/attendance/attendance.html', ret)


class AttendanceInfoListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'owner__name', 'attendancetime', 'image',]
        filters = dict()
        #部门过滤条件
        # if request.user.department_id == 9:
        #     filters['belongs_to_id'] = request.user.id
        ret = dict(data=list(AttendanceInfo.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class AttendanceInfoCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()

        ret['form'] = AttendanceInfoCreateForm(user=request.user)
        # ret['user_info'] = user_info

        return render(request, 'oa/attendance/attendance_create.html', ret)

    def post(self, request):
        res = dict()
        attendanceinfo_create_form = AttendanceInfoCreateForm(request.POST,request.FILES or None,user=request.user)
        if attendanceinfo_create_form.is_valid():
            attendanceinfo_create_form.save()
            res['status'] = 'success'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(attendanceinfo_create_form.errors)
            attendanceinfo_create_form = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'attendanceinfo_create_form': attendanceinfo_create_form[0]
            }

        return HttpResponse(json.dumps(res), content_type='application/json')


class AttendanceInfoUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        status_list = []
        if 'id' in request.GET and request.GET['id']:
            attendanceinfo = get_object_or_404(AttendanceInfo, pk=request.GET['id'])
            ret['attendance'] = attendanceinfo
            ret['form'] = AttendanceInfoUpdateForm(instance=attendanceinfo,user=request.user)

        return render(request, 'oa/attendance/attendance_update.html', ret)

    def post(self, request):
        res = dict()
        attendanceinfo = get_object_or_404(AttendanceInfo, pk=request.POST['id'])
        attendanceinfo_update_form = AttendanceInfoUpdateForm(request.POST,request.FILES or None, instance=attendanceinfo,user=request.user)
        if attendanceinfo_update_form.is_valid():
            attendanceinfo_update_form.save()
            res['status'] = 'success'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(attendanceinfo_update_form.errors)
            attendanceinfo_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'Acl_form_errors': attendanceinfo_form_errors[0]
            }

        return HttpResponse(json.dumps(res), content_type='application/json')

class AttendanceInfoDetailView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            attendanceinfo = get_object_or_404(AttendanceInfo, pk=request.GET.get('id'))
            ret['attendance'] = attendanceinfo
            # ret['Acl_log'] = Acl_log
        return render(request, 'oa/attendance/attendance_detail.html', ret)


class AttendanceInfoDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            AttendanceInfo.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')