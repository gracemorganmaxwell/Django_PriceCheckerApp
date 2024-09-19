# templatetags/cart_filters.py
from django import template

register = template.Library()

@register.filter
def get_item_quantity(cart_items, product_id):
    """
    Custom template filter to get the quantity of an item from cart_items based on product_id.
    """
    return cart_items.get(product_id, {}).get('quantity', 0)
