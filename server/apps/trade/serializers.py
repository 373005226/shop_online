from rest_framework import serializers
import time
import re
from shop_online_backend.settings import REGEX_MOBILE
from goods.models import Goods,Integralgoods
from .models import ShoppingCart, OrderInfo, OrderGoods,IntegralgoodsCart,Orderintergralgoods
from goods.serializers import GoodsSerializer,IntegralgoodsSerializer,TableOrderGoodSerializer,GoodsspecificationSerializer
from utils.alipay import AliPay
from shop_online_backend.settings import private_key_path, ali_pub_key_path


class ShopCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ("goods", "nums")


class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, label="数量", min_value=1,
                                    error_messages={
                                        "min_value": "商品数量不能小于一",
                                        "required": "请选择购买数量"
                                    })

    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user
        nums = validated_data["nums"]
        goods = validated_data["goods"]
        # selected = validated_data['selected']

        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        # 修改商品数量
        instance.nums = validated_data["nums"]
        # instance.selected = validated_data['selected']
        instance.save()
        return instance


class IntegralgoodsCartDetailSerializer(serializers.ModelSerializer):
    goods = IntegralgoodsSerializer(many=False, read_only=True)

    class Meta:
        model = IntegralgoodsCart
        fields = ("id","goods","nums")


class IntegralgoodsCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, label="数量", min_value=1,
                                    error_messages={
                                        "min_value": "商品数量不能小于一",
                                        "required": "请选择购买数量"
                                    })

    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Integralgoods.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user
        nums = validated_data["nums"]
        goods = validated_data["goods"]

        existed = IntegralgoodsCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = IntegralgoodsCart.objects.create(**validated_data)

        return existed


class OrderGoodsSerialzier(serializers.ModelSerializer):
    # 这里是订单列表信息
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderIntegralgoodsSerialzier(serializers.ModelSerializer):
    inter_goods = IntegralgoodsSerializer(many=False)

    class Meta:
        model = Orderintergralgoods
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    # 这个是订单的列表详细信息，每次购买之后的商品都会变成订单，所有订单的所有状态都会显示，并且配置了支付宝的支付地址，支付后的信息才会修改状态为支付成功
    goods = OrderGoodsSerialzier(many=True)
    intergralgoods = OrderIntegralgoodsSerialzier(many=True)
    alipay_url = serializers.SerializerMethodField(read_only=True)
    # distributor = serializers.CharField(read_only=True)
    # trade_no = serializers.CharField(read_only=True)
    # signer_name = serializers.CharField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def get_alipay_url(self, obj):
        alipay = AliPay(
            appid="2016101200666258",
            app_notify_url="http://127.0.0.1:8000/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )

        url = alipay.direct_pay(
            subject=obj.order_sn,
            out_trade_no=obj.order_sn,
            total_amount=obj.order_mount,
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

        return re_url

    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    alipay_url = serializers.SerializerMethodField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')


    def get_alipay_url(self, obj):
        alipay = AliPay(
            appid="2016101200666258",
            app_notify_url="http://127.0.0.1:8000/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )

        url = alipay.direct_pay(
            subject=obj.order_sn,
            out_trade_no=obj.order_sn,
            total_amount=obj.order_mount,
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

        return re_url

    def generate_order_sn(self):
        # 当前时间+userid+随机数
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id,
                                                       ranstr=random_ins.randint(10, 99))

        return order_sn

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = "__all__"


class AllOrderGoodsSerialzier(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields ="__all__"


class AllIntegralGoodsSerialzier(serializers.ModelSerializer):
    inter_goods = IntegralgoodsSerializer(many=False)

    class Meta:
        model = Orderintergralgoods
        fields ="__all__"


class AllOrderSerializer(serializers.ModelSerializer):
    # goods = AllOrderGoodsSerialzier(many=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = OrderInfo
        # fields =('goods','order_mount','user','pay_status','add_time')
        fields ="__all__"


class TableOrderGoodsSerialzier(serializers.ModelSerializer):
    # 这里是订单列表信息
    goods = TableOrderGoodSerializer(many=False)

    class Meta:
        model = OrderGoods
        # fields = ('goods',)
        fields = "__all__"


class TableOrderSerializer(serializers.ModelSerializer):
    goods = TableOrderGoodsSerialzier(many=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = OrderInfo
        fields =('goods','order_mount','user','add_time')


class AllOrderDetailSerializer(serializers.ModelSerializer):
    goods = AllOrderGoodsSerialzier(many=True)
    intergralgoods = AllIntegralGoodsSerialzier(many=True)

    class Meta:
        model = OrderInfo
        fields ="__all__"


class ExtractSerializer(serializers.Serializer):
    """
        这里是简单的发送修改手机号功能
    """
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        return mobile


class InformationCodeSerializer(serializers.Serializer):
    """
        这里是简单的发送自提验证码信息
    """
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        return mobile
