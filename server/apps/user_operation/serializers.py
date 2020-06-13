from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav
from .models import *
from goods.serializers import *


class UserFavDetailSerializer(serializers.ModelSerializer):
    # 这个是用户的收藏详情序列化
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserFavSerializer(serializers.ModelSerializer):
    # 这个有点是收藏的序列化，因为要判断是否被收藏，所以下面这里有个联合查询，如果已经收藏商品就会判断已经收藏
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

        fields = ("user", "goods", "id")


class AddressSerializer(serializers.ModelSerializer):
    # 这个是用户的个人收货地址栏
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "address", "signer_name", "add_time", "signer_mobile")


class Integral_calculationSeSerializer(serializers.ModelSerializer):
    """
        积分系统的序列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = integral_calculation
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
        这个是查看评论信息序列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    # goods = GoodsSerializer(many=False) #这个字段是为了显示商品的名字和图片信息，只需要goods的包含这两个字段的序列化即可
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Comment
        fields = "__all__"


class CommentDetailSerializer(serializers.ModelSerializer):
    """
        这个是查看评论信息序列化
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    goods = GoodsSerializer(many=False) #这个字段是为了显示商品的名字和图片信息，只需要goods的包含这两个字段的序列化即可
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Comment
        fields = "__all__"