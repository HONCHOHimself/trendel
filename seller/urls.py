from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('create-seller/<user_token>/', views.create_seller),
    path('update-seller/<user_token>/', views.update_seller),
    path('get-seller/<user_token>/', views.get_seller),

    path('create-category/', views.create_category),
    path('get-category/<category_id>/', views.get_category),
    path('get-categories/', views.get_categories),

    path('create-coupon/<user_token>/', views.create_coupon),
    path('update-coupon/<user_token>/', views.update_coupon),
    path('get-coupon/<user_token>/', views.get_coupon),
    path('get-coupons/<user_token>/', views.get_coupons),

    path('set_coupon_to_product/<product_id>/<coupon_id>/', views.set_coupon_to_product),

    path('create-product/<user_token>/<category_id>/', views.create_product),
    path('get-products/', views.get_products),
    path('get-products-by-category/<category_id>/', views.get_products_by_category),
    path('get-product/<product_id>/', views.get_product),
    path('get-product-off-price/<product_id>/', views.get_product_off),
    path('delete-product/<product_id>/', views.delete_product),

    path('add-product-size/<product_id>/', views.add_product_size),
    path('get-product-sizes/<product_id>/', views.get_product_sizes),
    path('delete-product-size/<product_size_id>/', views.delete_product_size),

    path('add-product-image/<product_id>/', views.add_product_image),
    path('delete-product-image/<product_image_id>/', views.delete_product_image),
]
