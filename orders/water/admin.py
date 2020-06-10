from django.contrib import admin

from .models import Order, Product, ProductOrder, Profile

admin.site.register(ProductOrder)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
