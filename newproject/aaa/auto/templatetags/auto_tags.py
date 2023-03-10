from django import template
from auto.models import *

register = template.Library()

@register.simple_tag()
def get_brands():
    return Brands.objects.all()