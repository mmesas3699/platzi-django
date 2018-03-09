from django.contrib import admin
from products.models import (
    Product, ProductImage, ProduCategory,
    LogBuy
)

class ProductImageInLine(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ProductImageInLine
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProduCategory)
admin.site.register(LogBuy)
