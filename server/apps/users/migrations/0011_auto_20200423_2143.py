# Generated by Django 2.2.9 on 2020-04-23 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200315_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default.png', help_text='用户头像', null=True, upload_to='avatar/', verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', help_text='性别', max_length=6, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='integral',
            field=models.IntegerField(default=0, help_text='积分', verbose_name='积分'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='isfaith',
            field=models.BooleanField(default=False, help_text='是否违约', verbose_name='是否违约'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='member_status',
            field=models.CharField(choices=[('primary', '初级会员'), ('senior', '高级会员')], default='primary', help_text='会员等级', max_length=30, verbose_name='会员等级'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, help_text='电话', max_length=11, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, help_text='昵称', max_length=30, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('ordinary_user', '普通用户'), ('order_distributor', '订单分配员'), ('picker', '商品拣货员'), ('delivery', '送货员'), ('shop_inspector', '超市自提商品管理员'), ('manager', '后台管理员'), ('boss', '超级管理员')], default='ordinary_user', help_text='角色', max_length=30, verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='code',
            field=models.CharField(help_text='验证码', max_length=10, verbose_name='验证码'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='mobile',
            field=models.CharField(help_text='电话', max_length=11, verbose_name='电话'),
        ),
    ]