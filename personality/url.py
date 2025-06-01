from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = ([
    path('', views.home.as_view(), name='home'),
    path('contact/', views.contactView.as_view(), name='contact'),
    path('services/popup/<int:pk>/', views.service_popup, name='service_popup'),
    path('projects/popup/<int:pk>/', views.project_popup, name='project_popup'),

               ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
