from django.contrib import admin

from shop.models import Item


@admin.register(Item)
class Itemadmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'description', 'price')
