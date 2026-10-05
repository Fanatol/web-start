from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "in_stock", "created_at", "quantity"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "description"]


admin.site.register(Product, ProductAdmin)
