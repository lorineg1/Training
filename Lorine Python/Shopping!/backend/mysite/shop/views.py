from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, Welcome to My Store")

def viewProduct(request, id):
    return HttpResponse(id)