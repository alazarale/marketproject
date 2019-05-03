from django.db import models
from django.contrib.auth.models import User

class AddressModel(models.Model):
    city = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city

class BusinessAcountModel(models.Model):
    user = models.ForeignKey(User, related_name='business_account', on_delete=models.PROTECT)
    business_type = models.CharField(max_length=100)
    comp_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    address = models.ForeignKey(AddressModel, related_name='business_account', on_delete=models.PROTECT)
    description = models.TextField()


    def __str__(self):
        return self.comp_name

class ProductModel(models.Model):
    user = models.ForeignKey(BusinessAcountModel, related_name='products', on_delete=models.PROTECT)
    product_name = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=100)
    description = models.TextField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    discount = models.FloatField()
    published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.product_name

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='images', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/name/images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductColorModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='color_choice', on_delete=models.PROTECT)
    color_name = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color_name


class ProductRateModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='rates', on_delete=models.PROTECT)
    rater = models.ForeignKey(User, related_name='rates', on_delete=models.PROTECT)
    comment = models.TextField()
    rate_value = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rate_value
