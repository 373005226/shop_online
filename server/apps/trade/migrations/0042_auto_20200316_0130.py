# Generated by Django 2.2.9 on 2020-03-16 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0041_auto_20200316_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integralgoodscart',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Integralgoods', verbose_name='积分兑换商品'),
        ),
        migrations.AlterField(
            model_name='orderintergralgoods',
            name='inter_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Integralgoods', verbose_name='积分商品'),
        ),
    ]
