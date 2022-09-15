from django.db import models
from django.contrib.auth.models import User

from django.core.validators import validate_image_file_extension

# Create your models here.
id_choices = {
    ("Aadhar Card", "Aadhar Card"),
    ("PAN Card", "PAN Card"),
}

class Seller(models.Model):
    shop_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    seller_user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_is_registered =  models.BooleanField(default=False)
    seller_ID_method = models.CharField(choices=id_choices, max_length=20, null=True, blank=True)
    seller_ID = models.CharField(max_length=12, unique=True, null=True, blank=True)
    shop_address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=10, unique=True, null=True, blank=True)
    seller_registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shop_name} - {self.seller_user}"
    
    class Meta:
        ordering = ['-seller_registered_at']


class Subcategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    category_image = models.ImageField(validators=[validate_image_file_extension], null=True, blank=True)
    category_image_2 = models.ImageField(validators=[validate_image_file_extension], null=True, blank=True)

    def __str__(self):
        return f'{self.category_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    category_image = models.ImageField(validators=[validate_image_file_extension], null=True, blank=True)
    category_image_2 = models.ImageField(validators=[validate_image_file_extension], null=True, blank=True)
    sub_categories = models.ManyToManyField(Subcategory)

    def __str__(self):
        return f'{self.id} - {self.category_name}'

    class Meta:
        verbose_name_plural  = 'Category'


class Coupon(models.Model):
    code = models.CharField(max_length=15, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code}'


size_choices = (
    ("xs", "xs"),
    ("s", "s"),
    ("m", "m"),
    ("L", "L"),
    ("XL", "XL"),
    ("xxL", "xxL"),
    ("XxxL", "XxxL"),
)

class Size(models.Model):
    size = models.CharField(max_length=60, choices=size_choices)

    def __str__(self):
        return f"{self.size} - Sizes"


class Image(models.Model):
    product_image = models.ImageField(upload_to='product_images', validators=[validate_image_file_extension])


class Product(models.Model):
    product_name = models.CharField(max_length=60)
    product_category = models.ManyToManyField(Category)
    product_primary_image = models.ImageField(upload_to='product_image', validators=[validate_image_file_extension], null=True, blank=True)
    product_images = models.ManyToManyField(Image)
    price = models.FloatField()
    offer_price = models.FloatField(null=True, blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)
    material_type = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    size = models.ManyToManyField(Size, blank=True, null=True)
    generic_name = models.CharField(max_length=60, blank=True, null=True)
    fit_type = models.CharField(max_length=60, blank=True, null=True)
    material_composition = models.CharField(max_length=60, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    product_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_published_at = models.DateTimeField(auto_now_add=True)

    @property
    def discount_percentage(self):
        pass

    def __str__(self):
        return f"{self.product_name} -{self.product_seller}"

    class Meta:
        ordering = ['-product_seller', '-product_published_at']
