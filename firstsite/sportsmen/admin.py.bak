from django.contrib import admin
from .models import Sportsman

@admin.register(Sportsman)
class SportsmanAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time_create', 'is_published')
    list_filter = ('is_published', 'time_create')
    search_fields = ('title', 'content')

