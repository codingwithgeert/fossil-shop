from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','available', 'created']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
    
admin.site.register(Product, ProductAdmin)