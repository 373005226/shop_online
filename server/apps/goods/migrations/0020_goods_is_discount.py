# Generated by Django 2.2.9 on 2020-04-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0019_goods_is_refund'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='is_discount',
            field=models.BooleanField(default=True, verbose_name='是否可以用优惠券'),
        ),
    ]