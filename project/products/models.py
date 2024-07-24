from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category/',default='/default.png')
    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product/',default='/default.png')
    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"