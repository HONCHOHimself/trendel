from django.shortcuts import render
from django.utils import timezone

# Models & Serializers
from customer.models import Order, GiftProduct, ProductReview
from customer.serializers import OrderSerializer, GiftProductSerializer, ProductReviewSerializer
from .models import Seller, Category, Coupon, Product, Size, Image
from .serializers import UserSerializer, SellerSerializer, CategorySerializer, CouponSerializer, ProductSerializer,\
							SizeSerializer, ImageSerializer

# Rest Framework
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET', 'POST'])
def create_seller(request, user_token):
	shop_name = request.data.get('shop_name')
	seller_name = request.data.get('seller_name')
	seller_ID_method = request.data.get('seller_ID_method')
	seller_ID = request.data.get('seller_ID')
	shop_address = request.data.get('shop_address')
	phone_no = request.data.get('phone_no')
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	if Seller.objects.filter(seller_user=user).exists():
		return Response('User is already a seller.')
	seller = Seller(shop_name=shop_name, seller_name=seller_name, seller_user=user,\
					seller_ID_method=seller_ID_method, seller_ID=seller_ID, shop_address=shop_address,\
					phone_no=phone_no)
	seller.save()
	return Response(True)


@api_view(['GET', 'POST'])
def update_seller(request, user_token):
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	seller = Seller.objects.filter(seller_user=user).first()
	if request.data.get('shop_name'):
		seller.shop_name = request.data.get('shop_name')
	if request.data.get('seller_name'):
		seller.seller_name = request.data.get('seller_name')
	if request.data.get('seller_ID_method'):
		seller.seller_ID_method = request.data.get('seller_ID_method')
	if request.data.get('seller_ID'):
		seller.seller_ID = request.data.get('seller_ID')
	if request.data.get('shop_address'):
		seller.shop_address = request.data.get('shop_address')
	if request.data.get('phone_no'):
		seller.phone_no = request.data.get('phone_no')
	seller.save()
	return Response(True)


@api_view(['GET'])
def get_seller(request, user_token):
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	seller = Seller.objects.filter(seller_user=user).first()
	serializer = SellerSerializer(seller)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_category(request):
	category_name = request.data.get('category_name')
	category_image = request.FILES.get('category_image')
	category_image_2 = request.FILES.get('category_image_2')
	category = Category(category_name=category_name, category_image=category_image,\
						category_image_2=category_image_2)
	category.save()
	return Response(True)


@api_view(['GET'])
def get_category(request, category_id):
	category = Category.objects.filter(id=category_id).first()
	serializer = CategorySerializer(category)
	return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):
	categories = Category.objects.all()
	serializer = CategorySerializer(categories, many=True)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_coupon(request, user_token):
	code = request.data.get('code')
	amount = request.data.get('amount')
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	seller = Seller.objects.filter(seller_user=user).first()
	coupon = Coupon(code=code, amount=amount, author=seller)
	coupon.save()
	return Response(True)


@api_view(['GET', 'POST'])
def update_coupon(request, user_token):
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	seller = Seller.objects.filter(seller_user=user).first()
	coupon = Coupon.objects.filter(author=seller).first()
	if request.data.get('code'):
		coupon.code = request.data.get('code')
	if request.data.get('amount'):
		coupon.amount = request.data.get('amount')
	coupon.save()
	return Response(True)


@api_view(['GET', 'POST'])
def get_coupon(request, user_token):
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	seller = Seller.objects.filter(seller_user=user).first()
	coupon = Coupon.objects.filter(author=seller).first()
	serializer = CouponSerializer(coupon)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_coupons(request, user_token):
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	seller = Seller.objects.filter(seller_user=user).first()
	coupon = Coupon.objects.filter(author=seller).all()
	serializer = CouponSerializer(coupon, many=True)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def set_coupon_to_product(request, product_id, coupon_id):
	product = Product.objects.filter(id=product_id).first()
	coupon = Coupon.objects.filter(id=coupon_id).first()
	product.coupon = coupon
	product.save()
	return Response(True)


@api_view(['GET', 'POST'])
def create_product(request, user_token, category_id):
	product_name = request.data.get('product_name')
	product_primary_image = request.FILES.get('product_primary_image')
	product_image = request.FILES.get('product_image')
	price = request.data.get('price')
	offer_price = request.data.get('offer_price')
	material_type = request.data.get('material_type')
	description = request.data.get('description')
	size = request.data.get('size')
	generic_name = request.data.get('generic_name')
	fit_type = request.data.get('fit_type')
	material_composition = request.data.get('material_composition')
	quantity = request.data.get('quantity')
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	seller = Seller.objects.filter(seller_user=user).first()
	product_published_at = timezone.now()
	product_category = Category.objects.filter(id=category_id).first()
	image = Image(product_image=product_image)
	image.save()
	product = product_category.product_set.create(
		product_name=product_name,
		product_primary_image=product_primary_image,
		price=price,
		offer_price=offer_price,
		material_type=material_type,
		description=description,
		generic_name=generic_name,
		fit_type=fit_type,
		material_composition=material_composition,
		quantity=quantity,
		product_seller=seller,
		product_published_at=product_published_at)
	image.product_set.add(product)
	return Response(True)


@api_view(['GET'])
def get_products(request):
	products = Product.objects.all()
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def get_products_by_category(request, category_id):
	category = Category.objects.filter(id=category_id).first()
	products = Product.objects.filter(product_category=category).all()
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def get_product(request, product_id):
	product = Product.objects.filter(id=product_id).first()
	serializer = ProductSerializer(product)
	return Response(serializer.data)


@api_view(['GET'])
def get_product_off(request, product_id):
	product = Product.objects.filter(id=product_id).first()
	if product.offer_price:
		off_price = (product.price / product.offer_price) % 100
		return Response(off_price)
	else:
		return Response(False)


@api_view(['GET'])
def delete_product(request, product_id):
	product = Product.objects.filter(id=product_id).first()
	product.delete()
	return Response(True)


@api_view(['GET', 'POST'])
def add_product_size(request, product_id):
	size = request.data.get('size')
	product = Product.objects.filter(id=product_id).first()
	try:
		size = Size(size=size)
		size.save()
		size.product_set.add(product)
		return Response(True)
	except:
		return Response(False)


@api_view(['GET', 'POST'])
def get_product_sizes(request, product_id):
	product = Product.objects.filter(id=product_id).first()
	sizes = product.size_set.all()
	serializer = SizeSerializer(sizes, many=True)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def delete_product_size(request, product_size_id):
	product_size = Size.objects.filter(id=product_size_id).first()
	product_size.delete()
	return Response(True)


@api_view(['GET', 'POST'])
def add_product_image(request, product_id):
	product_image = request.FILES.get('product_image')
	product = Product.objects.filter(id=product_id).first()
	try:
		image = Image(product_image=product_image)
		image.save()
		image.product_set.add(product)
		return Response(True)
	except:
		return Response(False)


@api_view(['GET', 'POST'])
def delete_product_image(request, product_image_id):
	product_image = Image.objects.filter(id=product_image_id).first()
	product_image.delete()
	return Response(True)
