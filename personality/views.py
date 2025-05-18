from django.shortcuts import render
from django.views.generic import TemplateView
from .models import User, Projects, Services, Work_Resume


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
