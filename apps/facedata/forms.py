from .models import FaceData
from django import forms
from django.forms import widgets
from django.contrib.auth import get_user_model

User = get_user_model()

class FaceDataForm(forms.ModelForm):
    class Meta:
        model = FaceData
        fields = '__all__'
        widgets = {
            'owner': widgets.Select(attrs={"class": " select2", "name": "owner", 'style': 'width:100%;'}),
            'face_id': widgets.Input(attrs={"class": "form-control pull-right  ", }, ),
            'face_name': widgets.Input(attrs={'class': "form-control", 'rows': "3"}),
            'face_image_url': widgets.Input(attrs={"class": "form-control pull-right f", }),
        }


class FaceDataCreateForm(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super(FaceDataCreateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            # department = user.department
            # post = user.post
            # if post == '部门安全管理员':
            #     self.fields['owner'].queryset = User.objects.filter(department=department)
            # else:
            #     self.fields['owner'].queryset = User.objects.filter(pk=user.id)
            pass

    class Meta:
        model = FaceData
        fields = '__all__'
        widgets = {
            'owner': widgets.Select(attrs={"class": " select2", "name": "owner", 'style': 'width:100%;'}),
            'face_id': widgets.Input(attrs={"class": "form-control pull-right  ",}, ),
            'face_name': widgets.Input(attrs={'class': "form-control", 'rows': "3"}),
            'face_image_url': widgets.Input(attrs={"class": "form-control pull-right f",} ),
        }
        error_messages = {
            "owner": {"required": "请选择对应人员"},

        }

class FaceDataUpdateForm(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super(FaceDataUpdateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            # department = user.department
            # post = user.post
            # if post == '部门安全管理员':
            #     self.fields['owner'].queryset = User.objects.filter(department=department)
            # else:
            #     self.fields['owner'].queryset = User.objects.filter(pk=user.id)
            pass


    class Meta:
        model = FaceData
        fields = '__all__'
        widgets = {
            'owner': widgets.Select(attrs={"class": " select2", "name": "owner", 'style': 'width:100%;'}),
            'face_id': widgets.Input(attrs={"class": "form-control pull-right  ", }, ),
            'face_name': widgets.Input(attrs={'class': "form-control", 'rows': "3"}),
            'face_image_url': widgets.Input(attrs={"class": "form-control pull-right f", }),
        }
        error_messages = {
            "owner": {"required": "请选择对应人员"},

        }

