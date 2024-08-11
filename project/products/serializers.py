from rest_framework import serializers  
from .models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Category 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):  
    category = serializers.CharField(read_only= True,source= 'category_id.name')
    class Meta:  
        model = Product 
        fields = ['name','category','description','image','price','carat','color','weight','material']

class ProductsSerializer(serializers.ModelSerializer):  
    category = serializers.CharField(read_only= True,source= 'category_id.name')
    class Meta:  
        model = Product 
        fields = ['id','name','description','category','image','price']