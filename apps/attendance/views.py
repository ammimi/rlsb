import json
import re

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.db.models import Q
import datetime


from system.mixin import LoginRequiredMixin
from .models import AttendanceInfo
from .forms import AttendanceInfoForm,AttendanceInfoCreateForm,AttendanceInfoUpdateForm
from system.models import Role,Menu,Structure,WorktimeSet
from system.models import SystemSetup
from facedata.models import FaceData
import xlwt
from io import StringIO,BytesIO
from apps.utils.workDays import workDays

User = get_user_model()
def addOneDay(daystr):
    addday = datetime.datetime.strptime(daystr, "%Y-%m-%d")+datetime.timedelta(days=1)
    return addday.strftime("%Y-%m-%d")



class AttendanceInfoView(LoginRequiredMixin, View):

    def get(self, request):
        ret = Menu.get_menu_by_request_url(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        role = request.user.roles.first().name  # 能登录的人都有角色
        if role == '系统管理员':
            ret = dict(structures=Structure.objects.all())
        elif role == '公司级管理员':
            ret = dict(structures=Structure.objects.filter(tree_id=request.user.department.tree_id))
        elif role == '部门管理员':
            ret = dict(structures=Structure.objects.filter(id=request.user.department.id))

        ret['titles'] = ('序号','姓名','部门','考勤时间','考勤状态','考勤图片','详情')
        ret['form'] = AttendanceInfoForm(user=request.user)

        return render(request, 'oa/attendance/attendance.html', ret)


class AttendanceInfoListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'facedata__face_cname','facedata__department__name', 'recorded_datetime', 'state','image',]
        filters = dict()
        if 'facedata__id' in request.GET and request.GET['facedata__id']:
            filters['facedata__id'] = request.GET['facedata__id']
        if 'date_range' in request.GET and request.GET['date_range']:
            date_range = request.GET['date_range'].split(' - ')
            start_date = date_range[0]
            end_date = addOneDay(date_range[1])
            print(end_date)
            filters['recorded_datetime__range'] = (start_date, end_date)
        if 'department' in request.GET and request.GET['department']:
            filters['facedata__department'] = request.GET['department']
        #部门过滤条件
        # if request.user.department_id == 9:
        #     filters['belongs_to_id'] = request.user.id
        ret = dict(data=list(AttendanceInfo.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')

class AttendanceInfoExportView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'facedata__face_cname', 'recorded_datetime', 'image',]
        filters = dict()
        facedatas = []
        if 'facedata__id' in request.GET and request.GET['facedata__id']:
            facedatas = FaceData.objects.filter(id=request.GET['facedata__id'])
        if 'date_range' in request.GET and request.GET['date_range']:
            date_range = request.GET['date_range'].split(' - ')
            start_date = date_range[0]
            # end_date = addOneDay(date_range[1])
            end_date = date_range[1]
        if 'department' in request.GET and request.GET['department']:
            structure = Structure.objects.get(id=request.GET['department'] )
            if structure.level  == 0:# 公司
                facedatas = FaceData.objects.filter(department__tree_id= structure.tree_id).order_by('department')
            else:#部门
                facedatas = FaceData.objects.filter(department=structure)
        # 如果他没有选，就导出他最大的权限的数据
        if not facedatas:

            role = request.user.roles.first().name  # 能登录的人都有角色
            if role == '系统管理员':
                facedatas = FaceData.objects.all().order_by('department')
            elif role == '公司级管理员':
                facedatas = FaceData.objects.filter(department__tree_id= request.user.department.tree_id).order_by('department')
            elif role == '部门管理员':
                facedatas = FaceData.objects.filter(department=request.user.department)



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
        sheet_prd.write_merge(0,0,0, 1, '考勤日期', style_heading)
        try:
            sheet_prd.write_merge(0,0,2, 3, date_range, style_heading)
            sheet_prd.write_merge(1, 1, 0, 1, '工作日', style_heading)
            up = start_date.split('-')
            down = end_date.split('-')
            startdate = datetime.datetime(int(up[0]), int(up[1]), int(up[2]),)
            enddate = datetime.datetime(int(down[0]), int(down[1]), int(down[2]),)
            work = workDays(startdate, enddate)

            sheet_prd.write_merge(1, 1, 2, 3, work.daysCount(), style_heading)

            '''
            facedata--
            '''
            sheet_prd.write(3,0,'编号')
            sheet_prd.write(3, 1, '姓名')
            sheet_prd.write(3, 2, '部门')
            sheet_prd.write(3, 3, '迟到')
            sheet_prd.write(3, 4, '早退')
            sheet_prd.write(3, 5, '旷工')
            indexday = 0
            for j in work.workDays():
                sheet_prd.write(3,6+indexday,j.strftime("%Y-%m-%d"))
                indexday =indexday +1
            row = 4

            num_yc = 0  #异常考勤数
            for facedata in facedatas:
                sheet_prd.write(row,0,str(row-2))
                sheet_prd.write(row,1,facedata.face_cname)
                sheet_prd.write(row,2,facedata.department.name)

                index_i = 0
                num_cd = 0  #迟到数
                num_zt = 0 #早退数
                num_kg = 0 #旷工数

                #求出facadata 的上下班时间
                company = Structure.objects.get(tree_id=facedata.department.tree_id,level=0)
                worktime  =  WorktimeSet.objects.get(company=company)
                uptime = worktime.uptime
                downtime = worktime.downtime


                for i in work.workDays():
                    uprecord = AttendanceInfo.objects.filter(state='上班考勤',facedata=facedata,recorded_datetime__date=i.date())
                    downrecord = AttendanceInfo.objects.filter(state='下班考勤',facedata=facedata,recorded_datetime__date=i.date())
                    checkrecord = ''
                    if uprecord:
                        checkrecord = checkrecord+'上班:'+uprecord[0].recorded_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        if uprecord[0].recorded_datetime.time() > uptime:
                            num_cd = num_cd +1
                    else:
                        num_kg = num_kg + 1
                    if downrecord:
                        checkrecord =checkrecord+'下班:'+downrecord[0].recorded_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        if downrecord[0].recorded_datetime.time() < downtime:
                            num_zt = num_zt +1
                    if uprecord and not downrecord:
                        if uprecord[0].recorded_datetime.time() < uptime:
                            num_zt = num_zt + 1

                    sheet_prd.write(row,6+index_i,checkrecord)
                    index_i = index_i+1

                sheet_prd.write(row, 3, str(num_cd))
                sheet_prd.write(row, 4, str(num_zt))
                sheet_prd.write(row, 5, str(num_kg))
                row = row +1

                num_yc = num_yc + num_cd + num_zt + num_kg
                #填入统计数据：
            sheet_prd.write_merge(2, 2, 0, 1, '异常考勤次数', style_heading)
            sheet_prd.write_merge(2, 2, 2, 3, str(num_yc), style_heading)
        except:
            sheet_prd.write_merge(0, 0, 2, 3, '请选择考勤日期', style_heading)




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



