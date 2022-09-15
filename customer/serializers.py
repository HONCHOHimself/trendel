from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order, GiftProduct, ProductReview

# Create your serializers here.
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email']

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['id', 'ordered', 'reciever_name', 'phone_no', 'street_address', 'zipcode', 'order_quantity',\
					'ordered_by', 'status', 'ordered_at']


class GiftProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = GiftProduct
		fields = ['id', 'product', 'order', 'recipient_name', 'message', 'sender_name']


class ProductReviewSerializer(serializers.ModelSerializer):
	author = UserSerializer()
	class Meta:
		model = ProductReview
		fields = ['id', 'product_reviewed', 'author', 'rating', 'photo', 'message', 'reviewed_at']
