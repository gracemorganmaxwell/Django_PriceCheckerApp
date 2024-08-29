from django.db import models

# # Create your models here.
# # class User(models.Model):
# #     username = models.CharField(max_length=250)
# #     first_name = models.CharField(max_length=250)  ----- Unnecessary?  
# #     last_name = models.CharField(max_length=250)
# #     email = models.CharField(max_length=250)
# #     password = models.CharField(max_length=250)

#     def __str__(self):
#         return self.username


class Supermarket(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    opening_hours = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} at {self.supermarket.name}: ${self.price}"