from django.contrib import admin
from .models import Category, Product, Image, Video
from django.db import models
from django import forms
from custom_translate.templatetags.custom_translation_tags import translate_number
from custom_translate.templatetags.persian_calendar_convertor import convert_to_persian_calendar ,format_persian_datetime
from django.contrib.auth.models import User, Group
import locale
from import_export.admin import ImportExportModelAdmin
from .resource import ProductResource
from django.contrib.admin import AdminSite 
locale.setlocale(locale.LC_ALL, 'en_US')

admin.site.unregister(User)
admin.site.unregister(Group)

def fa_num(num):
    return translate_number(locale.format_string("%d", num, grouping=True))

class ProductAdmin(ImportExportModelAdmin):
    search_fields = ("name",'id','description','price','created_at')
    list_display = ('pid','name','formatted_price','category_id', 'datetime')
    list_display_links = ('pid','name',)
    list_filter = ('category_id','created_at')
    actions = ('delete_image','set_price_to_zero',)
    resource_class = ProductResource

    def delete_image(self, request, queryset):
        queryset.update(image='/default.png')
        self.message_user(request, "تصاویر محصولات انتخاب شده حذف شدند")
    delete_image.short_description = "حذف تصویر محصولات انتخاب شده"

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)
        self.message_user(request, "قیمت محصولات انتخاب شده صفر شدند")
    set_price_to_zero.short_description = "صفر کردن قیمت محصولات انتخاب شده"

    def datetime(self, obj):
        return translate_number(format_persian_datetime(convert_to_persian_calendar(obj.created_at)))
    datetime.short_description = 'منتشر شده در'
    datetime.admin_order_field = 'price'

    def pid(self, obj):
        return fa_num(obj.id)
    pid.short_description = 'کد محصول'
    pid.admin_order_field = 'price'

    def formatted_price(self, obj):   
        return f"{fa_num(obj.price)} تومان "
    formatted_price.short_description = 'قیمت'
    formatted_price.admin_order_field = 'price'

    formfield_overrides = {
        models.IntegerField: {'widget': forms.NumberInput(attrs={'size':'50'})},
        models.TextField: {"widget": forms.Textarea()},
    }

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",'description')
    list_display = ('name',)
    actions = ('delete_image',)

    def delete_image(self, request, queryset):
        queryset.update(image='/default.png')
        self.message_user(request, "تصاویر دسته بندی های انتخاب شده حذف شدند")
    delete_image.short_description = "حذف تصویر دسته بندی های انتخاب شده"

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image','product_id', 'datetime')
    search_fields = ("product_id",'image')
    list_filter = ('uploaded_at','product_id')

    def datetime(self, obj):
        return translate_number(format_persian_datetime(convert_to_persian_calendar(obj.uploaded_at)))
    datetime.short_description = 'منتشر شده در'

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video','product_id', 'datetime')
    search_fields = ("product_id",'video')
    list_filter = ('uploaded_at','product_id')

    def datetime(self, obj):
        return translate_number(format_persian_datetime(convert_to_persian_calendar(obj.uploaded_at)))
    datetime.short_description = 'منتشر شده در'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)