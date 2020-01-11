from django.contrib import admin
from .models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('realtor', 'title')
    list_per_page = 25
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

admin.site.register(Listing, ListingAdmin)