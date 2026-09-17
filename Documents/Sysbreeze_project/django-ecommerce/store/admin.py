from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'created_at')
	list_display_links = ('name',)
	search_fields = ('name',)
	list_filter = ('created_at',)
	date_hierarchy = 'created_at'
	ordering = ('-created_at',)
	list_per_page = 25
	readonly_fields = ('created_at',)
