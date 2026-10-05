from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "category",
        "price",
        "in_stock",
        "created_at",
        "quantity",
    ]
    list_display_links = ["id", "name"]
    search_fields = ["name", "description"]
    list_filter = ["category", "in_stock"]
    list_editable = ["price", "in_stock"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
В