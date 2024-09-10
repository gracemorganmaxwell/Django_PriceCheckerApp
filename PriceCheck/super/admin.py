from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import SupermarketChain, Store, Product, PriceHistory, UserStorePreference, Profile

# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(SupermarketChain)
class SuperAdmin(admin.ModelAdmin):
    list_display = ("chain_id", "chain_name")
    list_filter = ("chain_name",)
    search_fields = ["chain_name"]
    list_editable = ('chain_name',)

    class Meta:
        ordering = ["chain_name",]

    fieldsets = (
        ("Name of Supermarket Chain", {'fields': ("chain_name",)}),
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_id", 'product_name', 'unit_type', 'product_code', 'unit_price')
    list_filter = ("product_name", "product_code")
    search_fields = ["product_name", "product_code"]

    class Meta:
        ordering = ["product_name", "product_code",]

    fieldsets = (
        ("Product", {'fields': ("product_name", "product_code", "unit_type", "unit_price", "on_sale")}),
    )

@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ("product_id", 'date', 'price', 'on_sale', 'store_id')
    list_filter = ("product_id", "price")
    search_fields = ["product_id", "price", 'on_sale','store_id']

    class Meta:
        ordering = ["product_id", "price",]

    fieldsets = (
        ("Price History", {'fields': ("product_id", "price", "on_sale")}),
    )

@admin.register(UserStorePreference)
class UserStorePreferenceAdmin(admin.ModelAdmin):
    list_display = ("USP_id", "user", 'store')
    list_filter = ("user", "store")
    search_fields = ["user__username", "store__store_name"]

    class Meta:
        ordering = ["user", "store",]

    fieldsets = (
        ("User Store Preference", {'fields': ("user", "store")}),
    )

# Register Store model if it's not already registered
admin.site.register(Store)
