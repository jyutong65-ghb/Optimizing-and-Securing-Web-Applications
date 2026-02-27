from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sports/', views.sports, name='sports'),
    path('sports/<int:sp_id>/', views.sports, name='sports_by_id'),
    re_path(r'^sports/(?P<year>[0-9]{4})/$', views.sports_by_year, name='sports_by_year'),
]
