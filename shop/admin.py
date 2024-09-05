from django.contrib import admin
from .models import Category, Product

# Default: Administracion de Django
admin.site.site_header = "Administracion Plants & Gifts"

# Default: Sitio administrativo
admin.site.index_title = "Panel de control"

# Default: Sitio administrativo
admin.site.site_title = "Plants & Gifts"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name",)}
