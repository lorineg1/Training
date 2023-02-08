from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('full_name', instance.username)

        instance.save()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'