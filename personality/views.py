from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse

from .forms import ContactForm
from .models import User, Projects, Services, Work_Resume, Contact


# Create your views here.
class home(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        user_setting: User = User.objects.filter(is_main_setting=True).first()
        context['user_setting'] = user_setting
        context['sazmani_project'] = Projects.objects.filter(project_category='سازمانی')
        context['shopping_project'] = Projects.objects.filter(project_category='فروشگاهی')
        context['amoozeshi_project'] = Projects.objects.filter(project_category='آموزشی')
        context['services'] = Services.objects.all()
        context['all_resume'] = Work_Resume.objects.all()
        return context


class contactView(CreateView):
    form_class = ContactForm
    template_name = 'base.html'
    success_url = '/contact/'

    def form_valid(self, form):
        response = super().form_valid(form)
        instance = form.save()
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                "status": "success",
                "message": f"{instance.first_name} عزیز، پیام شما با موفقیت ارسال شد!"
            })
        return response

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                "status": "error",
                "message": "لطفاً تمام فیلدها را به درستی پر کنید."
            }, status=400)
        return super().form_invalid(form)


def service_popup(request, pk):
    service = get_object_or_404(Services, pk=pk)
    all_services = Services.objects.all()
    print("SERVICE TITLE:", service.title)
    return render(request, 'partial/single_service.html',
                  {'service': service,
                        'all_services':all_services})


def project_popup(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    return render(request, 'partial/project_modal_content.html',
                  {'project': project})
