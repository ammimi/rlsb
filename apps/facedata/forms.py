from .models import FaceData
from system.models import Structure
from django import forms
from django.forms import widgets
from django.contrib.auth import get_user_model
from django.forms.widgets import ClearableFileInput
User = get_user_model()

class ImageWidget(ClearableFileInput):
    template_with_initial = (
        '%(initial_text)s: <a href="%(initial_url)s"><img width="100px" height="100px" src="%(initial_url)s"></a> '
        '%(clear_template)s<br />%(input_text)s: %(input)s'
    )

    template_with_clear = ''

class FaceDataForm(forms.ModelForm):
    class Meta:
        model = FaceData
        fields = '__all__'
        widgets = {

            'face_id': widgets.Input(attrs={"class": "form-control pull-right  ", }, ),
            'face_name': widgets.Input(attrs={'class': "form-control", 'rows': "3"}),
            'face_image_url': widgets.Input(attrs={"class": "form-control pull-right f", }),
        }


class FaceDataCreateForm(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super(FaceDataCreateForm, self).__init__(*args, **kwargs)
        role = user.roles.first().name  # 能登录的人都有角色
        if role == '系统管理员':
            self.fields['department'].queryset = Structure.objects.all()
        elif role == '公司级管理员':
            self.fields['department'].queryset = Structure.objects.filter(tree_id=user.department.tree_id)

    class Meta:
        model = FaceData
        fields = '__all__'
        widgets = {
            'name': widgets.Input(attrs={"class": "form-control pull-right  ", }, ),
            'birthday':widgets.Input(attrs={"class": "form-control pull-right form_datetime ",'readonly': 'readonly'}, ),
            'gender':widgets.Select(attrs={"class": " select2", "name": "gender", 'style': 'width:100%;'}),
            'mobile':widgets.Input(attrs={"class": "form-control pull-right  ", }, ),
            'joindate':widgets.Input(attrs={"class": "form-control pull-right form_datetime ",'readonly': 'readonly'}, ),
            'department':widgets.Select(attrs={"class": " select2", "name": "department", 'style': 'width:100%;'}),

            'face_id': widgets.Input(attrs={"class": "form-control pull-right  ",}, ),
            'face_name': widgets.Input(attrs={'class': "form-control", 'rows': "3"}),
            'face_image': widgets.ClearableFileInput(attrs={'class': "form-control", 'rows': "3"}),
        }


class FaceDataUpdateForm(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super(FaceDataUpdateForm, self).__init__(*args, **kwargs)
        role = user.roles.first().name  # 能登录的人都有角色
        if role == '系统管理员':
            self.fields['department'].queryset = Structure.objects.all()
        elif role == '公司级管理员':
            self.fields['department'].queryset = Structure.objects.filter(tree_id=user.department.tree_id)

    class Meta:
        model = FaceData
        fields = '__all__'
        widgets = {
            'name': widgets.Input(attrs={"class": "form-control pull-right  ", }, ),
            'birthday': widgets.Input(
                attrs={"class": "form-control pull-right form_datetime ", 'readonly': 'readonly'}, ),
            'gender': widgets.Select(attrs={"class": " select2", "name": "gender", 'style': 'width:100%;'}),
            'mobile': widgets.Input(attrs={"class": "form-control pull-right  ", }, ),
            'joindate': widgets.Input(
                attrs={"class": "form-control pull-right form_datetime ", 'readonly': 'readonly'}, ),
            'department': widgets.Select(attrs={"class": " select2", "name": "department", 'style': 'width:100%;'}),

            'face_id': widgets.Input(attrs={"class": "form-control pull-right  ", }, ),
            'face_name': widgets.Input(attrs={'class': "form-control", 'rows': "3"}),
            'face_image': widgets.ClearableFileInput(attrs={'class': "form-control", 'rows': "3"}),
        }

