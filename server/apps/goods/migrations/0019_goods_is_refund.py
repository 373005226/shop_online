# Generated by Django 2.2.9 on 2020-04-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0018_goods_goods_introduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='is_refund',
            field=models.BooleanField(default=False, verbose_name='是否支持退款'),
        ),
    ]
