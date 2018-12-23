
from django import forms
from .models import AttendanceInfo
from django.forms import widgets
from django.contrib.auth import get_user_model

User = get_user_model()

class AttendanceInfoForm(forms.ModelForm):
    class Meta:
        model = AttendanceInfo
        fields = '__all__'


class AttendanceInfoCreateForm(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super(AttendanceInfoCreateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            # department = user.department
            # post = user.post
            # if post == '部门安全管理员':
            #     self.fields['owner'].queryset = User.objects.filter(department=department)
            # else:
            #     self.fields['owner'].queryset = User.objects.filter(pk=user.id)
            pass

    class Meta:
        model = AttendanceInfo
        fields = '__all__'
        widgets = {
            'owner': widgets.Select(attrs={"class": " select2", "name": "owner", 'style': 'width:100%;'}),
            'attendancetime':widgets.Input(attrs={"class": "form-control pull-right form_datetime ",'readonly': 'readonly'}, ),
            'image': widgets.ClearableFileInput(attrs={'class': "form-control", 'rows': "3"}),

        }
        error_messages = {
            "owner": {"required": "请选择对应人员"},

        }

class AttendanceInfoUpdateForm(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super(AttendanceInfoUpdateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            # department = user.department
            # post = user.post
            # if post == '部门安全管理员':
            #     self.fields['owner'].queryset = User.objects.filter(department=department)
            # else:
            #     self.fields['owner'].queryset = User.objects.filter(pk=user.id)
            pass


    class Meta:
        model = AttendanceInfo
        fields = '__all__'
        widgets = {
            'owner': widgets.Select(attrs={"class": " select2", "name": "owner", 'style': 'width:100%;'}),
            'attendancetime': widgets.Input(
                attrs={"class": "form-control pull-right form_datetime ", 'readonly': 'readonly'}, ),
            'image': widgets.ClearableFileInput(attrs={'class': "form-control", 'rows': "3"}),

        }
        error_messages = {
            "owner": {"required": "请选择对应人员"},

        }