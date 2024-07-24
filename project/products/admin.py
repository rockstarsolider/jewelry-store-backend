from django.contrib import admin
from .models import Category, Product

# Register your models here.
class AdminSite(admin.AdminSite):
    site_header = "پنل ادمین"
    site_title = "Blog Post Admin Portal"
    index_title = "مدیریت وبسایت"

admin_site = AdminSite(name='admin_site')

admin_site.register(Category)
admin_site.register(Product)