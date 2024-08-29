from django.contrib import admin
from .models import User, Supermarket, Product, Price

# Register your models here.
admin.site.register(User)
admin.site.register(Supermarket)
admin.site.register(Product)
admin.site.register(Price)