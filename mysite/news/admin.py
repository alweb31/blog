from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('category', 'is_published')
    list_filter = ('category', 'is_published')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(News, NewsAdmin)
