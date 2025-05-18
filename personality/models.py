from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    logo = models.ImageField(upload_to='media', blank=True, null=True,verbose_name='لوگو')
    avatar = models.ImageField(upload_to='media', blank=True, null=True,verbose_name='آوارتار')
    work_time = models.IntegerField(blank=True,null=True,verbose_name='سابقه کار به سال')
    projects = models.IntegerField(blank=True,null=True,verbose_name='تعداد پروژه های تکمیل شده')
    description = models.CharField(max_length=500, verbose_name='توضیحات')
    short_description = models.CharField(max_length=300, verbose_name='توضیحات کوتاه')
    mobile_number = models.CharField(max_length=11, verbose_name='شماره تماس')
    birthday = models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')
    is_main_setting = models.BooleanField(default=False,verbose_name='تنظیمات اصلی')
    resume = models.FileField(upload_to= 'media',blank=True, null=True, verbose_name='فایل رزومه' )


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.first_name

class Services(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان خدمت')
    short_description = models.CharField(max_length=300, verbose_name='توضیحات کوتاه')
    description = models.CharField(max_length=500, verbose_name='توضیحات')
    service_image = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='تصویر خدمت')


    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return self.title

class Projects(models.Model):
    project_title = models.CharField(max_length=300, verbose_name='عنوان پروژه')
    project_category = models.CharField(max_length=300, verbose_name='دسته بندی')
    strat_date = models.DateField(blank=True, null=True, verbose_name='تاریخ شروع')
    end_date = models.DateField(blank=True, null=True, verbose_name='تاریخ پایان')
    customer = models.CharField(max_length=300, verbose_name='مشتری')
    front_end = models.CharField(max_length=300, verbose_name='طراح')
    image_1 = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='تصویر اول')
    image_2 = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='تصویر دوم')
    image_3 = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='تصویر سوم')
    summary = models.CharField(max_length=500, verbose_name='خلاصه پروژه')

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def __str__(self):
        return self.project_title


class Work_Resume(models.Model):
    wr_title = models.CharField(max_length=300, verbose_name='عنوان رزومه')
    wr_company = models.CharField(max_length=300, verbose_name='شرکت')
    wr_start_date = models.DateField(blank=True, null=True, verbose_name='تاریخ شروع به کار')
    wr_end_date = models.DateField(blank=True, null=True, verbose_name='تاریخ پایان کار')
    wr_task = models.CharField(max_length=300, verbose_name='وظایف و دستاوردها')



    class Meta:
        verbose_name = 'سابقه کار'
        verbose_name_plural = 'سوابق کاری'

    def __str__(self):
        return self.wr_title
