from django import template
from b1.models import *

register = template.Library()


@register.simple_tag()
def get_partners():
    return Footer.objects.all()