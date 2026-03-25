from django.contrib import admin
from .models import Sportsman, Sports

class SportsmanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'sport')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'sport')

class SportsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Sportsman, SportsmanAdmin)
admin.site.register(Sports, SportsAdmin)
