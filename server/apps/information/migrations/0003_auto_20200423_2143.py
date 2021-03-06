# Generated by Django 2.2.9 on 2020-04-23 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_auto_20200316_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilevisitnumber',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='访问时间', verbose_name='访问时间'),
        ),
        migrations.AlterField(
            model_name='mobilevisitnumber',
            name='count',
            field=models.IntegerField(default=0, help_text='网站访问总次数', verbose_name='网站访问总次数'),
        ),
        migrations.AlterField(
            model_name='pcvisitnumber',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='访问时间', verbose_name='访问时间'),
        ),
        migrations.AlterField(
            model_name='pcvisitnumber',
            name='count',
            field=models.IntegerField(default=0, help_text='网站访问总次数', verbose_name='网站访问总次数'),
        ),
    ]
