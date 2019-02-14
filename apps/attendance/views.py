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
from .forms import AttendanceInfoForm
import xlwt
from io import StringIO,BytesIO


User = get_user_model()


class AttendanceInfoView(LoginRequiredMixin, View):

    def get(self, request):
        ret = Menu.get_menu_by_request_url(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        ret['titles'] = ('姓名','考勤时间','考勤图片','详情')
        ret['form'] = AttendanceInfoForm()
        return render(request, 'oa/attendance/attendance.html', ret)


class AttendanceInfoListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'facedata__face_cname', 'recorded_datetime', 'image',]
        filters = dict()
        if 'facedata__id' in request.GET and request.GET['facedata__id']:
            filters['facedata__id'] = request.GET['facedata__id']
        if 'date_range' in request.GET and request.GET['date_range']:
            date_range = request.GET['date_range'].split(' - ')
            start_date = date_range[0]
            end_date = date_range[1]
            filters['recorded_datetime__range'] = (start_date, end_date)
            print (filters['recorded_datetime__range'])
        #部门过滤条件
        # if request.user.department_id == 9:
        #     filters['belongs_to_id'] = request.user.id
        ret = dict(data=list(AttendanceInfo.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')

class AttendanceInfoExportView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'facedata__face_cname', 'recorded_datetime', 'image',]
        filters = dict()
        if 'facedata__id' in request.GET and request.GET['facedata__id']:
            filters['facedata__id'] = request.GET['facedata__id']
        if 'date_range' in request.GET and request.GET['date_range']:
            date_range = request.GET['date_range'].split(' - ')
            start_date = date_range[0]
            end_date = date_range[1]
            filters['recorded_datetime__range'] = (start_date, end_date)


        #部门过滤条件
        # if request.user.department_id == 9:
        #     filters['belongs_to_id'] = request.user.id
        rets = AttendanceInfo.objects.filter(**filters)

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response[
            'Content-Disposition'] = 'attachment;filename={0}.xls'.format('考勤信息')
        wb = xlwt.Workbook(encoding='utf-8')
        sheet_prd = wb.add_sheet('考勤信息')
        style_heading = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index white,
                    bold on,
                    height 0xA0;
                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour 0x19;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                                    )
        style_body = xlwt.easyxf("""
                font:
                    name Arial,
                    bold off,
                    height 0XA0;
                align:
                    wrap on,
                    vert center,
                    horiz left;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                                 )
        style_green = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x11;")
        style_red = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x0A;")
        fmts = [
            'M/D/YY',
            'D-MMM-YY',
            'D-MMM',
            'MMM-YY',
            'h:mm AM/PM',
            'h:mm:ss AM/PM',
            'h:mm',
            'h:mm:ss',
            'M/D/YY h:mm',
            'mm:ss',
            '[h]:mm:ss',
            'mm:ss.0',
        ]
        style_body.num_format_str = fmts[0]
        # 1st line
        sheet_prd.write(0, 0, '序列号', style_heading)
        sheet_prd.write(0, 1, '姓名', style_heading)
        sheet_prd.write(0, 2, '考勤日期', style_heading)
        row = 1
        for ret in rets:
            sheet_prd.write(row, 0, row, style_heading)
            sheet_prd.write(row, 1, ret.facedata.face_cname, style_body)
            sheet_prd.write(row, 2, ret.recorded_datetime, style_body)
            row += 1

        output = BytesIO()
        wb.save(output)
        output.seek(0)
        response.write(output.getvalue())
        return response


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



