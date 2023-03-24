from django import template
register = template.Library()

from ..models import order_Card

@register.simple_tag
def total_orders():
    return order_Card.title.value