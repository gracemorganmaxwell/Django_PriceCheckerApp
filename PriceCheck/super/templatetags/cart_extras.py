from django import template

register = template.Library()

@register.filter
def dict_item(dictionary, key):
    if isinstance(dictionary, dict):
        # Convert key to string to ensure compatibility
        return dictionary.get(str(key), 0)
    return 0