from django.urls import path
from . import views
from .views import SportsmenHome, SportsmenSport, ShowPost, AddArticle

urlpatterns = [
    path('', SportsmenHome.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('addarticle/', AddArticle.as_view(), name='add_article'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('sport/<slug:sport_slug>/', SportsmenSport.as_view(), name='sport'),
]
