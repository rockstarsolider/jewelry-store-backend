from rest_framework import serializers  
from .models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Category 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):  
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    category = serializers.CharField(read_only= True,source= 'category_id.name')
    class Meta:  
        model = Product 
        fields = '__all__'