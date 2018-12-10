from django.views.generic import TemplateView

from .mixin import LoginRequiredMixin
from django.views.generic.base import View
from .models import Structure, Menu,SystemSetup
from django.shortcuts import render
from .forms import SystemSetupForm
from django.http import HttpResponse
import json
from apps.custom import SandboxCreateView, SandboxUpdateView, BreadcrumbMixin


class SystemView(LoginRequiredMixin, BreadcrumbMixin, TemplateView):

    template_name = 'system/system_index.html'

class SystemSetupView(LoginRequiredMixin, View):
    """
    系统基本配置：create
    """

    def get(self, request):
        ret = Menu.get_menu_by_request_url(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'system/tools/system-setup.html', ret)

    def post(self, request):
        res = dict(result=False)
        system_setup_form = SystemSetupForm(request.POST)
        if system_setup_form.is_valid():
            system_setup_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')

