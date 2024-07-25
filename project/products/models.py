from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name=('نام دسته بندی'))
    description = models.TextField(blank=True, null=True,verbose_name=('توضیحات'))
    image = models.ImageField(upload_to='category/',default='/default.png',verbose_name=('تصویر'))
    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"
    def __str__(self):
        return self.name

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products',verbose_name=('دسته بندی'))
    name = models.CharField(max_length=100,verbose_name=('نام محصول'))
    description = models.TextField(blank=True, null=True,verbose_name=('توضیحات'))
    price = models.PositiveIntegerField(default=0,verbose_name=('قیمت'))
    image = models.ImageField(upload_to='product/',default='/default.png',verbose_name=('تصویر'))
    created_at = jmodels.jDateField(auto_now_add=True, blank=True,verbose_name=('منتشر شده در '))
    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"
    def __str__(self):
        return self.name