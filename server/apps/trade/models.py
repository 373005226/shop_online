from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods,Integralgoods
User=get_user_model()
# Create your models here.


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, verbose_name="用户",on_delete=models.CASCADE,help_text="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品",on_delete=models.CASCADE,help_text="商品")
    nums = models.IntegerField(default=0, verbose_name="购买数量",help_text="购买数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


class IntegralgoodsCart(models.Model):
    """
        用户积分商品
    """
    user = models.ForeignKey(User, verbose_name="用户",on_delete=models.CASCADE,help_text="用户")
    goods = models.ForeignKey(Integralgoods, verbose_name="积分兑换商品",on_delete=models.CASCADE,blank=True,null=True,help_text="积分兑换商品")
    nums = models.IntegerField(default=0, verbose_name="购买数量",help_text="购买数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = '用户积分商品'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS = (
        ("paying", "待支付"),
        # ("TRADE_SUCCESS", "成功"),
        # ("TRADE_CLOSED", "超时关闭"),
        # ("WAIT_BUYER_PAY", "交易创建"),
        ("refunding", "退款申请中"),
        ("fefunding","退款成功，交易结束"),
        ("Picking","订单商品配货中"),  #拣货人员，提取货物给送货人员
        ("Picking_complete","订单配货完成"),  #拣货人员，提取货物给送货人员
        ("checkout","商品二次检验完"),  #线下，二次检验等待用户提取
        ("Delivery", "等待送货员提取商品"),  #送货人员状态
        ("Deliverying", "订单商品送货中"),  #送货人员状态
        ("trade_evaluate", "交易结束等待评价"),  #交易完成等待评价
        ("TRADE_SUCCESS", "交易结束")#交易结束
    )
    user = models.ForeignKey(User, verbose_name="用户",on_delete=models.CASCADE,help_text="用户")
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号",help_text="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="交易号",help_text="交易号")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="订单状态",help_text="订单状态")
    # post_script = models.CharField(max_length=200, verbose_name="订单留言",null=True,blank=True)
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额",help_text="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间",help_text="支付时间")
    takegoods_status=models.CharField(choices=(('online','线上'),('self_mention','线下自提')),default="online",max_length=30,verbose_name='提取方式',blank=True,help_text="提取方式")
    gettime =  models.CharField(default='',max_length=100,verbose_name='取得订单货品时间',help_text="取得订单货品时间")
    address = models.CharField(max_length=100, default="", verbose_name="收货地址",help_text="收货地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人",help_text="签收人")
    picker = models.CharField(max_length=20, default="", verbose_name="订单拣货人",null=True,blank=True,help_text="订单拣货人")
    inspecter = models.CharField(max_length=20, default="", verbose_name="订单二次拣货人",null=True,blank=True,help_text="订单二次拣货人")
    distributor = models.CharField(max_length=20, default="", verbose_name="订单分配员",null=True,blank=True,help_text="订单分配员")
    deliveryman = models.CharField(verbose_name="订单配送人员",default='',null=True,blank=True,max_length=15,help_text="订单配送人员")
    deliveryman_phone = models.CharField(max_length=11,default='',null=True,blank=True,verbose_name='配送人员手机号',help_text="配送人员手机号")
    picker_time= models.CharField(max_length=100,default='',verbose_name='订单拣货时间',blank=True,null=True,help_text="订单拣货时间")
    inspecter_time= models.CharField(max_length=100,default='',verbose_name='订单二次验货时间',blank=True,null=True,help_text="订单二次验货时间")
    distributor_time= models.CharField(max_length=100,default='',verbose_name='订单分配时间',blank=True,null=True,help_text="订单分配时间")
    delivery_time =  models.CharField(max_length=100,default='',verbose_name='订单配送时间',blank=True,null=True,help_text="订单配送时间")
    success_time = models.CharField(max_length=100,default='',verbose_name='交易完成时间',blank=True,null=True,help_text="交易完成时间")
    singer_mobile = models.CharField(max_length=11, verbose_name="联系电话",blank=True,help_text="联系电话")
    isdoubt = models.BooleanField(default=False,verbose_name='是否为有疑问订单',help_text="是否为有疑问订单")
    remarks= models.CharField(max_length=100,default='',null=True,blank=True,verbose_name='订单配送备注',help_text="订单配送备注")
    doubttext = models.CharField(max_length=150,default='',null=True,blank=True,verbose_name='订单疑问原因',help_text="订单疑问原因")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    订单的商品详情
    """
    order = models.ForeignKey(OrderInfo, verbose_name="订单信息", related_name="goods",on_delete=models.CASCADE,help_text="订单信息")
    goods = models.ForeignKey(Goods, verbose_name="商品",on_delete=models.CASCADE,help_text="商品")
    # goods_price = models.CharField(default=0,verbose_name='商品价格',max_length=100)
    goods_num = models.IntegerField(default=0, verbose_name="商品数量",help_text="商品数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)


class Orderintergralgoods(models.Model):
    """
    订单的积分兑换商品
    """
    order = models.ForeignKey(OrderInfo, verbose_name="订单信息", related_name="intergralgoods", on_delete=models.CASCADE,help_text="订单信息")
    inter_goods = models.ForeignKey(Integralgoods,verbose_name='积分商品',on_delete=models.CASCADE,help_text="积分商品")
    goods_num = models.IntegerField(default=0, verbose_name="积分兑换商品数量",help_text="积分兑换商品数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "积分兑换商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)


class ExtractCode(models.Model):
    """
        短信验证码
    """
    code=models.CharField(max_length=10,verbose_name="验证码",help_text="验证码")
    mobile=models.CharField(max_length=11,verbose_name="电话",help_text="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class InformationCode(models.Model):
    """
        发送提取消息的短信
    """
    mobile=models.CharField(max_length=11,verbose_name="电话",help_text="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "发送的自提短信码"
        verbose_name_plural = verbose_name