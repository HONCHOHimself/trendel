from django.contrib import admin
from .models import Order, GiftProduct, ProductReview

# Register your models here.
admin.site.register(Order)
admin.site.register(GiftProduct)
admin.site.register(ProductReview)
