# Generated by Django 2.2.9 on 2020-04-22 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0021_auto_20200420_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(help_text='轮播图图片', max_length=200, upload_to='brands/', verbose_name='轮播图图片'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='is_hot',
            field=models.BooleanField(default=False, help_text='是否放上品牌特卖', verbose_name='是否放上品牌特卖'),
        ),
    ]
