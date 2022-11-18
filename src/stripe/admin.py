from django.contrib import admin

from src.stripe.models import Item
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_photo', 'price', 'currency',)

    def get_photo(self, obj):
        """Show photo in admin panel"""
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='60'>")
        else:
            return 'Нет фото'
