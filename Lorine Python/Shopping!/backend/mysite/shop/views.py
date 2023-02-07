from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

def index(request):
    num_products = Product.objects.all().count()
    return HttpResponse("Hi, Welcome to My Store, I smell like shit")

def viewProduct(request, id):
    response = "You are looking at Category."
    Product_Category = Product.objects.filter(category = 'shirts')
    return HttpResponse(response % id)

def home(request):
    category = Category.objects.all().filter(parent=None)
    post_by_category = Product.objects.filter(category__category_name = "aaa", published = True)
    slider = Product.objects.filter(slider = True).order_by('-created_on')
    context = {
        'category' : category,
        'post_by_category' : post_by_category,
        'slider' : slider,
    } 
    return render(request, 'home.html', context)