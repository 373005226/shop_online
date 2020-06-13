# Generated by Django 2.2.9 on 2020-02-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20200223_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('TRADE_CLOSED', '未付款交易超时关闭，或支付完成后全额退款'), ('WAIT_BUYER_PAY', '交易创建，等待买家付款'), ('TRADE_SUCCESS', '交易支付成功'), ('TRADE_FINISHED', '交易结束，不可退款'), ('refunding', '待退款'), ('refund', '退款成功'), ('loading', '等待配送'), ('writing', '待评价'), ('TRADE_SUCCESS', '订单已完成')], default='paying', max_length=30, verbose_name='订单状态'),
        ),
    ]
