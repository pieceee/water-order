from django.contrib import admin

from .models import Order
from .models import Product
from .models import ProductOrder
from .models import Profile

admin.site.register(ProductOrder)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
