from rest_framework import viewsets
from rest_framework import mixins
from users.serializers import UserMemberSerializer
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# from .models import UserFav, UserLeavingMessage, UserAddress
from utils.permissions import IsOwnerOrReadOnly
# from .serializers import UserFavSerializer, UserFavDetailSerializer, AddressSerializer, LeavingMessageSerializer


class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    #这个是用户信息的收藏函数，如果有人收藏了商品，这个商品的收藏数就+1
    """
    list:
        获取用户收藏列表
    retrieve:
        判断某个商品是否已经收藏
    create:
        收藏商品
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     goods = instance.goods
    #     goods.fav_num += 1
    #     goods.save()

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer
        return UserFavSerializer


class AddressViewset(viewsets.ModelViewSet):
    # 这个是用户的地址栏，ModelViewSet可以对商品进行增删改查，get_queryset就是可以对于一个视频
    """
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    read:
        查看收货地址详情
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class CommonSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    """
    个人评论表管理
    list:
        查看自己评论过的信息
    create:
        添加商品评论
    delete:
        删除商品评论
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication )
    # serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return CommentDetailSerializer
        return CommentSerializer


class UserMemberViewSet(mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
        用户的会员信息表
    """
    serializer_class = UserMemberSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication )

    def get_queryset(self):
        """
            get方法只显示自己的信息
        :return:
        """
        return User.objects.filter(username=self.request.user)

    def get_object(self):
        """
            无论参数是什么都只请求到自己的信息
        :return: self.user
        """
        return self.request.user

    def get_permissions(self):
        """
            如果是要修改就必须要登录，如果是要创建就返回为空
        :return:
        """
        if self.action == "retrieve":
            return [IsAuthenticated()]
        elif self.action == "create":
            return []

        return []


class Integral_calculationSeSerializerViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """
        积分系统使得用户可以通过积分去换购商品
    """
    serializer_class = Integral_calculationSeSerializer
    queryset = integral_calculation.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication )
