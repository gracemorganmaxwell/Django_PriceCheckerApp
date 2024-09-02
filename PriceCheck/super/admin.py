from django.contrib import admin
from .models import SupermarketChain, Store, Product, PriceHistory, User, UserStorePreferance
from django.db import models

class SuperInline(admin.TabularInline):
    model = SupermarketChain
    extra = 1
    fields=('chain_name')


# Register your models here.
# @admin.register(SupermarketChain)
# class SuperAdmin(admin.ModelAdmin):
#     list_display = ("chain_id", "chain_name")

# admin.site.register(models.SupermarketChain)

@admin.register(SupermarketChain)
class SuperAdmin(admin.ModelAdmin):
    list_display = ("chain_id", "chain_name")
    list_filter = ("chain_name",)
    search_fields = ["chain_name"]
    list_editable = ('chain_name',)
    class Meta:
        ordering = ["chain_name",]
    fieldsets=(
        ("Name of Supermarket Chain", {'fields':("chain_name",)}),
    )

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("store_id", 'store_name', 'store_adress','store_region', 'chain_id') 
    list_filter = ("store_name", "store_region")
    search_fields = ["store_name", "store_region"]
    class Meta:
        ordering = ["store_name",]
    fieldsets=(
        ("Store location", {'fields':("store_name", "store_region")}),
    )
  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_id", 'product_name', 'unit_type', 'store_id', 'product_code', 'unit_price')   
    list_filter = ("product_name", "product_code")
    search_fields = ["product_name", "prodcut_code"]
    class Meta:
        ordering = ["product_name", "product_code",]
    fieldsets=(
        ("Product", {'fields':("product_name", "product_code")}),
    )


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ("product_id", 'date','price', 'on_sale')   
    list_filter = ("product_id", "price")
    search_fields = ["product_id", "price", 'on_sale',]
    class Meta:
        ordering = ["product_id", "price",]
    def on_sale(self, obj):
        return "Yes"

    fieldsets=(
        ("Price History", {'fields':("product_id", "price")}),
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name","user_user_name", 'user_email','user_type') 
    list_filter = ("user_name", "user_user_name", "user_type")
    search_fields = ["user_name", "user_username", "user_type",]
    class Meta:
        ordering = ["user_name", "user_type",]
    fieldsets=(
        ("Users", {'fields':("user_name", "user_type")}),
    )
  

@admin.register(UserStorePreferance)
class UserStorePrefernaceAdmin(admin.ModelAdmin):
    list_display = ("USP_id","user_id", 'store_id')   
    list_filter = ("user_id", "store_id")
    search_fields = ["user_id", "store_id"]
    class Meta:
        ordering = ["user_id", "store_id",]
    fieldsets=(
        ("User Store Preferance", {'fields':("user_id", "store_id")}),
    )

