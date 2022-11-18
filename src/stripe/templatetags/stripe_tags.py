from django import template

from src.stripe.models import Item

# регистрируем теги
register = template.Library()


@register.inclusion_tag("stripe/list_categories.html")
def show_items_list():
    items = Item.objects.all()
    return {"items": items}
