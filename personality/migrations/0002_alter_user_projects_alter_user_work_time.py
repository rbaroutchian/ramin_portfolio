# Generated by Django 5.2.1 on 2025-05-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='projects',
            field=models.IntegerField(blank=True, null=True, verbose_name='تعداد پروژه های تکمیل شده'),
        ),
        migrations.AlterField(
            model_name='user',
            name='work_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='سابقه کار به سال'),
        ),
    ]
