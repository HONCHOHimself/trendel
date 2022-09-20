from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
	path('create-order/<product_id>/<user_token>/', views.create_order),
		# reciever_name
		# phone_no
		# street_address
		# zipcode
		# order_quantity
	path('get-user-orders/<user_token>/', views.get_user_orders),
	path('get-order/<order_id>/', views.get_order),

	path('create-gift/<product_id>/<order_id>/', views.create_gift),
		# recipient_name
		# message
		# sender_name
	path('get-gifts/<order_id>/', views.get_gifts),

	path('create-review/<product_id>/<user_token>/', views.create_review),
		# rating
		# photo
		# message
	path('get-reviews/<product_id>/', views.get_reviews),

	path('search/', views.search),
		# user_input
]