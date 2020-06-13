from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from trade.models import OrderInfo
from goods.models import Goods
# Create your models here.
User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户",on_delete=models.CASCADE,help_text="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品", help_text="商品id",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(User, verbose_name="用户" ,on_delete=models.CASCADE,help_text="用户")
    province = models.CharField(max_length=100, default="", verbose_name="省份",help_text="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市",help_text="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域",help_text="区域")
    address = models.CharField(max_length=100, default="", verbose_name="详细地址",help_text="详细地址")
    signer_name = models.CharField(max_length=100, default="", verbose_name="签收人",help_text="签收人")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="电话",help_text="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address


class integral_calculation(models.Model):
    """
    计算用户够买后的积分
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE,help_text="用户")
    integral_nums= models.ForeignKey(OrderInfo, verbose_name="订单金额", help_text="订单金额", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = '用户积分'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user

