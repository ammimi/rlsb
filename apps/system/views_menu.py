from django.views.generic import ListView

from .mixin import LoginRequiredMixin
from apps.custom import SandboxCreateView, SandboxUpdateView, BreadcrumbMixin
from .models import Menu,Structure
from django.shortcuts import render
from django.views.generic.base import View
import  json
from django.db.models import Q


class MenuCreateView(SandboxCreateView):
    model = Menu
    fields = '__all__'

    def get_context_data(self, **kwargs):
        kwargs['menu_all'] = Menu.objects.all()
        return super().get_context_data(**kwargs)


class MenuListView(LoginRequiredMixin, BreadcrumbMixin, ListView):
    model = Menu
    context_object_name = 'menu_all'


class MenuUpdateView(SandboxUpdateView):
    model = Menu
    fields = '__all__'
    template_name_suffix = '_update'

    def get_context_data(self, **kwargs):
        kwargs['menu_all'] = Menu.objects.all()
        return super().get_context_data(**kwargs)

class getMenuTree:
    def getStructure(self):
        fields = ['id', 'name', 'parent__id', ]
        structures = list(Structure.objects.all().values(*fields))
        return  structures

    def getChildren(self,id=None):
        sz=[]
        structures = self.getStructure()
        for obj in structures:
            if obj["parent__id"] == id:
                sz.append({"id":obj["id"],"name":obj["name"],"children":self.getChildren(obj["id"])})
        return sz

    def print(self):
        sz = self.getChildren(id=None)
        print(json.dumps(sz,ensure_ascii=False))
        return json.dumps(sz,ensure_ascii=False)


class MenuTree(LoginRequiredMixin,View):
    def get(self,request):
        role = request.user.roles.all().order_by('id')[0].name
        if role == '系统管理员':
            nodes = Structure.objects.all()
        elif role == '公司级管理员':
            nodes = Structure.objects.filter(tree_id=request.user.department.tree_id)
        elif role == '部门管理员':#最多支持3级
            nodes = Structure.objects.filter(Q(tree_id=request.user.department.tree_id,level=1,id=request.user.department.id)|#一级
                                            Q(tree_id=request.user.department.tree_id,level=2,parent__id=request.user.department.id)|#二级
                                            Q(tree_id=request.user.department.tree_id,level=3,parent__parent__id=request.user.department.id)     #三级
                                               )

        return render(request, 'menutree.html',{'nodes':nodes})
