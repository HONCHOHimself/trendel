from django.shortcuts import render
from django.utils import timezone

# Models & Serializers
from .models import Order, GiftProduct, ProductReview
from .serializers import OrderSerializer, GiftProductSerializer, ProductReviewSerializer
from seller.models import Seller, Category, Coupon, Product
from seller.serializers import SellerSerializer, CategorySerializer, CouponSerializer, ProductSerializer

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET', 'POST'])
def create_order(request, product_id, user_token):

	reciever_name = request.data.get('reciever_name')
	phone_no = request.data.get('phone_no')
	street_address = request.data.get('street_address')
	zipcode = request.data.get('zipcode')
	order_quantity = request.data.get('order_quantity')

	product = Product.objects.filter(id=product_id).first()
	token = Token.objects.filter(key=user_token).first()
	user = token.user

	order = Order(ordered=product, reciever_name=reciever_name, phone_no=phone_no, street_address=street_address,\
				zipcode=zipcode, order_quantity=order_quantity, ordered_by=user, status='Pending')
	order.save()
	return Response(True)


@api_view(['GET'])
def get_user_orders(request, user_token):
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	order = Order.objects.filter(ordered_by=user).all()
	serializer = OrderSerializer(order, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def get_order(request, order_id):
	order = Order.objects.filter(id=order_id).first()
	serializer = OrderSerializer(order)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_gift(request, product_id, order_id):

	recipient_name = request.data.get('recipient_name')
	message = request.data.get('message')
	sender_name = request.data.get('sender_name')

	product = Product.objects.filter(id=product_id).first()
	order = Order.objects.filter(id=order_id).first()

	gift = GiftProduct(product=product, order=order, recipient_name=recipient_name, message=message,\
						sender_name=sender_name)
	gift.save()
	return Response(True)


@api_view(['GET'])
def get_gifts(request, order_id):
	order = Order.objects.filter(id=order_id).first()
	gift = GiftProduct.objects.filter(order=order).all()
	serializer = GiftProductSerializer(gift, many=True)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_review(request, product_id, user_token):

	rating = request.data.get('rating')
	photo = request.FILES.get('photo')
	message = request.data.get('message')

	product = Product.objects.filter(id=product_id).first()
	token = Token.objects.filter(key=user_token).first()
	user = token.user

	review = ProductReview(product_reviewed=product, author=user, rating=rating, photo=photo,\
							message=message)
	review.save()
	return Response(True)


@api_view(['GET'])
def get_reviews(request, product_id):
	reviews = ProductReview.objects.filter(product_reviewed=product_id).all()
	serializer = ProductReviewSerializer(reviews, many=True)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def search(request):
	user_input = request.data.get('user_input')
	categories = Category.objects.filter(category_name__icontains=user_input).all()
	serializer = CategorySerializer(categories, many=True)
	return Response(serializer.data)
