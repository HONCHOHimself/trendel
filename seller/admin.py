from django.contrib import admin
from .models import Seller, Category, Coupon, Product, Size, Image, Subcategory

# Register your models here.
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Coupon)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Subcategory)
