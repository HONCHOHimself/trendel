from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Seller, Category, Coupon, Product, Size, Image

# Create your serializers here.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'shop_name', 'seller_name', 'seller_user', 'shop_is_registered', 'seller_ID_method',\
                    'seller_ID', 'shop_address', 'phone_no', 'seller_registered_at']

class DemoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image', 'category_image_2']

class CategorySerializer(serializers.ModelSerializer):
    sub_categories = DemoCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image', 'category_image_2', 'sub_categories']

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'amount', 'author']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'size']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'product_image']


class ProductSerializer(serializers.ModelSerializer):
    product_images = ImageSerializer(many=True)
    size = SizeSerializer(many=True)
    product_category = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_category', 'product_primary_image', 'product_images', 'price', 'offer_price', 'coupon',\
                    'size', 'material_type', 'description', 'generic_name', 'fit_type', 'material_composition',\
                    'quantity', 'product_seller', 'product_published_at']
