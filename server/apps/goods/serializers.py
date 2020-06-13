from rest_framework import serializers
from .models import *
from users.serializers import UserGoodsSerializer


class CommentSerializer(serializers.ModelSerializer):
    """
        这个是查看评论信息序列化
    """
    user = UserGoodsSerializer(many=False)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Comment
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    """
    商品的轮播图信息
    """
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = GoodsImage
        fields = "__all__"


class AllOrderGoodSerializer(serializers.ModelSerializer):
    category = serializers.CharField(read_only=True)

    class Meta:
        model = Goods
        # fields = ('category',)
        fields = "__all__"


class IntegralgoodsSerializer(serializers.ModelSerializer):
    """
        积分商品
    """
    class Meta:
        model = Integralgoods
        fields ="__all__"


class GoodsspecificationSerializer(serializers.ModelSerializer):
    """
    商品的规格信息
    """
    class Meta:
        model = Goodsspecification
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    """
        商品信息
    """
    images = GoodsImageSerializer(many=True,read_only=True)
    specification =GoodsspecificationSerializer(many=True,read_only=True)
    comment = CommentSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"


class GoodsBaseSerializer(serializers.ModelSerializer):
    """
        商品的基本信息，用于评论信息的基本序列化
    """
    images = GoodsImageSerializer(many=True,read_only=True)

    class Meta:
        model = Goods
        fields= ('name','images')


class BannerIndexSerializer(serializers.ModelSerializer):
    """
        首页的轮播图
    """
    class Meta:
        model = BannerIndex
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
        这个是商品分类的序列化，但是为了让商品分类里面可以显示商品的信息，所以要吧商品序列化的结果作为商品分类的一个字段
    """
    goods_catelogy = GoodsSerializer(many=True,read_only=True)

    class Meta:
        model = GoodsCategoryAll
        fields = "__all__"


class TableOrderGoodSerializer(serializers.ModelSerializer):
    category = serializers.CharField(read_only=True)
    # specification =GoodsspecificationSerializer(many=True,read_only=True)

    class Meta:
        model = Goods
        fields = ('category',)
