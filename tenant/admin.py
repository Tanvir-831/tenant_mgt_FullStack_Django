from django.contrib import admin
from .models import Building, Flat

# Register your models here.

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'Location', 'District', 'post_code', 'total_flat', 'owner']
    search_fields = ['name', 'Location', 'District', 'post_code', 'total_flat', 'owner']
    list_filter = ['Location', 'District', 'post_code', 'total_flat']
    list_per_page = 10

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['number', 'owner', 'building', 'bedroom', 'washroom', 'kitchen', 'balcony', 'flat_area', 'tenant', 'rent']
    search_fields = ['number', 'owner', 'building', 'bedroom', 'washroom', 'kitchen', 'balcony', 'flat_area', 'tenant', 'rent']
    list_filter = ['owner', 'building', 'bedroom', 'washroom', 'kitchen', 'balcony', 'flat_area', 'tenant', 'rent']
    list_per_page = 10