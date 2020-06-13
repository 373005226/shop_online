from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
admin.site.site_header = "多购后台管理系统"
admin.site.site_title = '多购后台管理系统'


class CommentAdmin(admin.StackedInline):
    model = Comment


class GoodsCategoryAllResource(resources.ModelResource):
    class Meta:
        model = GoodsCategoryAll


@admin.register(GoodsCategoryAll)
class ProxyAdmin(ImportExportModelAdmin):
    resource_class = GoodsCategoryAllResource


class GoodImageInline(admin.StackedInline):
    model = GoodsImage
    extra = 1   #默认是3个


class Goodsspecification(admin.StackedInline):
    model = Goodsspecification
    extra = 1


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['category','name','fav_num','goods_num','sold_num','is_new','is_hot','is_normal','add_time']
    search_fields = ['name','is_new','is_hot','is_normal']
    inlines = (GoodImageInline,Goodsspecification,CommentAdmin)


class integralgoodsAdmin(admin.ModelAdmin):
    list_display = ['name','image','specification','integral','goods_num']


admin.site.register(Goods,GoodsAdmin)
admin.site.register(BannerIndex)
admin.site.register(GoodsCategoryBrand)
admin.site.register(Integralgoods,integralgoodsAdmin)