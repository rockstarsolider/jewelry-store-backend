from rest_framework.views import APIView
from rest_framework.response import Response   
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.core.paginator import Paginator,EmptyPage

class ProductList(APIView):  
    def get(self, request):  
        products = Product.objects.all()
        category_name = request.query_params.get('category')
        from_price = request.query_params.get('from')
        to_price = request.query_params.get('to')
        search = request.query_params.get('search')
        order = request.query_params.get('order', default='created_at')
        perpage = request.query_params.get('perpage',default= 20)
        page = request.query_params.get('page',default= 1)
        if category_name:
            products = products.filter(category_id__name = category_name)
        if from_price:
            products = products.filter(price__gte = from_price)
        if to_price:
            products = products.filter(price__lte = to_price)
        if search:
            products = products.filter(name__icontains = search)
        if order:
            products = products.order_by(order).reverse()
        paginator = Paginator(products, per_page=perpage)
        try:
            products = paginator.page(number=page)
        except EmptyPage:
            products = []
        serializer = ProductSerializer(products, many=True)  
        return Response(serializer.data) 

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many= True)
        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get(self, request, pk=None):
        product = Product.objects.get(pk = pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)