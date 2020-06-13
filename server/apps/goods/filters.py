import django_filters
from django.db.models import Q
from .models import *


class GoodsFilter(django_filters.rest_framework.FilterSet):
    min_price = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte',help_text="最低价格")
    max_price = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte',help_text="最高价格")
    is_new = django_filters.BooleanFilter(field_name="is_new",help_text="是否为新品")
    is_hot = django_filters.BooleanFilter(field_name="is_hot",help_text="是否为热门商品")
    is_normal = django_filters.BooleanFilter(field_name="is_normal",help_text="是否为上架商品")
    category_type = django_filters.NumberFilter(field_name="category",help_text="类别数目")

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'is_new', 'is_normal', 'is_hot', 'category_type']