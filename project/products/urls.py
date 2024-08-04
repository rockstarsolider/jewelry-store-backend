from django.urls import path  
from .views import ProductList,CategoryList,ProductDetail

urlpatterns = [  
    path('products/', ProductList.as_view(), name='product-list'), 
    path('ctegories/', CategoryList.as_view(), name='category-list'), 
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),  
] 