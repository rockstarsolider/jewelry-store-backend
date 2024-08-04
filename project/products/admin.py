from django.contrib import admin
from .models import Category, Product, Image, Video
from django.db import models
from django import forms

# Register your models here.
class AdminSite(admin.AdminSite):
    site_header = "پنل ادمین"
    site_title = "پنل ادمین"
    index_title = "مدیریت وبسایت"

admin_site = AdminSite(name='admin_site')

class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",'description')
    list_display = ('name','formatted_price','category_id', 'datetime')
    list_filter = ('category_id','created_at')
    actions = ('delete_image','set_price_to_zero',)

    def delete_image(self, request, queryset):
        queryset.update(image='/default.png')
        self.message_user(request, "تصاویر محصولات انتخاب شده حذف شدند")
    delete_image.short_description = "حذف تصویر محصولات انتخاب شده"

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)
        self.message_user(request, "قیمت محصولات انتخاب شده صفر شدند")
    set_price_to_zero.short_description = "صفر کردن قیمت محصولات انتخاب شده"

    def datetime(self, obj):  
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
    datetime.short_description = 'منتشر شده در'

    @admin.display(description='قیمت')
    def formatted_price(self, obj):   
        return f"{obj.price:,} تومان "
    # formatted_price.short_description = 'قیمت'

    formfield_overrides = {
        models.IntegerField: {'widget': forms.NumberInput(attrs={'size':'50'})},
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
    list_filter = ('uploaded_at',)

    def datetime(self, obj):  
        return obj.uploaded_at.strftime("%Y-%m-%d %H:%M:%S")
    datetime.short_description = 'منتشر شده در'

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video','product_id', 'datetime')
    search_fields = ("product_id",'video')
    list_filter = ('uploaded_at',)

    def datetime(self, obj):  
        return obj.uploaded_at.strftime("%Y-%m-%d %H:%M:%S")
    datetime.short_description = 'منتشر شده در'

admin_site.register(Category, CategoryAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(Image, ImageAdmin)
admin_site.register(Video, VideoAdmin)