from django.contrib import admin
from .models import Category, Product

# Register your models here.
class AdminSite(admin.AdminSite):
    site_header = "پنل ادمین"
    site_title = "پنل ادمین"
    index_title = "مدیریت وبسایت"

admin_site = AdminSite(name='admin_site')

class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",'description')
    list_display = ('name','price','category_id','created_at')
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

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",'description')
    list_display = ('name',)
    actions = ('delete_image',)

    def delete_image(self, request, queryset):
        queryset.update(image='/default.png')
        self.message_user(request, "تصاویر دسته بندی های انتخاب شده حذف شدند")
    delete_image.short_description = "حذف تصویر دسته بندی های انتخاب شده"

admin_site.register(Category, CategoryAdmin)
admin_site.register(Product, ProductAdmin)