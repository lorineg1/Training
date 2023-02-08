from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

def index(request):
    return HttpResponse("Hi, Welcome to My Store, I smell like shit")

def viewProduct(request, id):
    response = "You are viewing a Product"
    return HttpResponse(response % id)

def viewCategory(request, Category):
    response = "You are looking at Category."
    Product_Category = Product.objects.filter(Category)
    return HttpResponse(response % Product_Category)

def home(request):
    category = Category.objects.all().filter(parent=Category)
    post_by_category = Product.objects.filter(category__category_name = "aaa", published = True)
    slider = Product.objects.filter(slider = True).order_by('-created_on')
    context = {
        'category' : category,
        'post_by_category' : post_by_category,
        'slider' : slider,
    } 
    return render(request, 'home.html', context)

@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
        