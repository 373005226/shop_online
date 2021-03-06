# Generated by Django 2.2.9 on 2020-04-23 21:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0058_auto_20200422_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractcode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='extractcode',
            name='code',
            field=models.CharField(help_text='验证码', max_length=10, verbose_name='验证码'),
        ),
        migrations.AlterField(
            model_name='extractcode',
            name='mobile',
            field=models.CharField(help_text='电话', max_length=11, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='informationcode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='informationcode',
            name='mobile',
            field=models.CharField(help_text='电话', max_length=11, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='integralgoodscart',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='integralgoodscart',
            name='goods',
            field=models.ForeignKey(blank=True, help_text='积分兑换商品', null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Integralgoods', verbose_name='积分兑换商品'),
        ),
        migrations.AlterField(
            model_name='integralgoodscart',
            name='nums',
            field=models.IntegerField(default=0, help_text='购买数量', verbose_name='购买数量'),
        ),
        migrations.AlterField(
            model_name='integralgoodscart',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='goods',
            field=models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='goods_num',
            field=models.IntegerField(default=0, help_text='商品数量', verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(help_text='订单信息', on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='trade.OrderInfo', verbose_name='订单信息'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='address',
            field=models.CharField(default='', help_text='收货地址', max_length=100, verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='delivery_time',
            field=models.CharField(blank=True, default='', help_text='订单配送时间', max_length=100, null=True, verbose_name='订单配送时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='deliveryman',
            field=models.CharField(blank=True, default='', help_text='订单配送人员', max_length=15, null=True, verbose_name='订单配送人员'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='deliveryman_phone',
            field=models.CharField(blank=True, default='', help_text='配送人员手机号', max_length=11, null=True, verbose_name='配送人员手机号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='distributor',
            field=models.CharField(blank=True, default='', help_text='订单分配员', max_length=20, null=True, verbose_name='订单分配员'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='distributor_time',
            field=models.CharField(blank=True, default='', help_text='订单分配时间', max_length=100, null=True, verbose_name='订单分配时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='doubttext',
            field=models.CharField(blank=True, default='', help_text='订单疑问原因', max_length=150, null=True, verbose_name='订单疑问原因'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='gettime',
            field=models.CharField(default='', help_text='取得订单货品时间', max_length=100, verbose_name='取得订单货品时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='inspecter',
            field=models.CharField(blank=True, default='', help_text='订单二次拣货人', max_length=20, null=True, verbose_name='订单二次拣货人'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='inspecter_time',
            field=models.CharField(blank=True, default='', help_text='订单二次验货时间', max_length=100, null=True, verbose_name='订单二次验货时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='isdoubt',
            field=models.BooleanField(default=False, help_text='是否为有疑问订单', verbose_name='是否为有疑问订单'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_mount',
            field=models.FloatField(default=0.0, help_text='订单金额', verbose_name='订单金额'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_sn',
            field=models.CharField(blank=True, help_text='订单号', max_length=30, null=True, unique=True, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('paying', '待支付'), ('refunding', '退款申请中'), ('fefunding', '退款成功，交易结束'), ('Picking', '订单商品配货中'), ('Picking_complete', '订单配货完成'), ('checkout', '商品二次检验完'), ('Delivery', '等待送货员提取商品'), ('Deliverying', '订单商品送货中'), ('trade_evaluate', '交易结束等待评价'), ('TRADE_SUCCESS', '交易结束')], default='paying', help_text='订单状态', max_length=30, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_time',
            field=models.DateTimeField(blank=True, help_text='支付时间', null=True, verbose_name='支付时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='picker',
            field=models.CharField(blank=True, default='', help_text='订单拣货人', max_length=20, null=True, verbose_name='订单拣货人'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='picker_time',
            field=models.CharField(blank=True, default='', help_text='订单拣货时间', max_length=100, null=True, verbose_name='订单拣货时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='remarks',
            field=models.CharField(blank=True, default='', help_text='订单配送备注', max_length=100, null=True, verbose_name='订单配送备注'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='signer_name',
            field=models.CharField(default='', help_text='签收人', max_length=20, verbose_name='签收人'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='singer_mobile',
            field=models.CharField(blank=True, help_text='联系电话', max_length=11, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='success_time',
            field=models.CharField(blank=True, default='', help_text='交易完成时间', max_length=100, null=True, verbose_name='交易完成时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='takegoods_status',
            field=models.CharField(blank=True, choices=[('online', '线上'), ('self_mention', '线下自提')], default='online', help_text='提取方式', max_length=30, verbose_name='提取方式'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='trade_no',
            field=models.CharField(blank=True, help_text='交易号', max_length=100, null=True, unique=True, verbose_name='交易号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='orderintergralgoods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderintergralgoods',
            name='goods_num',
            field=models.IntegerField(default=0, help_text='积分兑换商品数量', verbose_name='积分兑换商品数量'),
        ),
        migrations.AlterField(
            model_name='orderintergralgoods',
            name='inter_goods',
            field=models.ForeignKey(help_text='积分商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Integralgoods', verbose_name='积分商品'),
        ),
        migrations.AlterField(
            model_name='orderintergralgoods',
            name='order',
            field=models.ForeignKey(help_text='订单信息', on_delete=django.db.models.deletion.CASCADE, related_name='intergralgoods', to='trade.OrderInfo', verbose_name='订单信息'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='goods',
            field=models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='nums',
            field=models.IntegerField(default=0, help_text='购买数量', verbose_name='购买数量'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
