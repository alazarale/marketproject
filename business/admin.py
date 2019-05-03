from django.contrib import admin
from .models import ProductColorModel, ProductImageModel, ProductModel, ProductRateModel, AddressModel, BusinessAcountModel

# Register your models here.
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ['color_name', 'product','created', 'updated']

admin.site.register(ProductColorModel, ProductColorAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'product','created', 'updated']

admin.site.register(ProductImageModel, ProductImageAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'tag_line', 'in_stock', 'price', 'discount', 'published', 'created', 'updated']

admin.site.register(ProductModel)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'zone', 'region', 'zip_code', 'created', 'updated']

admin.site.register(AddressModel, AddressAdmin)

class BusinessAcountAdmin(admin.ModelAdmin):
    list_display = ['business_type', 'comp_name', 'email', 'phone_number', 'address']

admin.site.register(BusinessAcountModel, BusinessAcountAdmin)

class ProductRateAdmin(admin.ModelAdmin):
    list_display = ['comment', 'rate_value', 'created', 'updated', 'product']

admin .site.register(ProductRateModel, ProductRateAdmin)