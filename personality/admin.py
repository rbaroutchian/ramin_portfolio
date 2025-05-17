from django.contrib import admin
from . import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email', 'mobile_number']


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title']


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'project_category', 'customer']


class Work_Resume_Admin(admin.ModelAdmin):
    list_display = ['wr_title','wr_title']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Services, ServicesAdmin)
admin.site.register(models.Projects, ProjectsAdmin)
admin.site.register(models.Work_Resume, Work_Resume_Admin)
