from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

admin.site.register(Blog,BlogAdmin)