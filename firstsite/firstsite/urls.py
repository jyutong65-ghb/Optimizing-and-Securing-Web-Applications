from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('<h1>Django Welcome Page</h1><p>First Assignment</p><p><a href="/sportsmen/">Go to Second Assignment</a></p>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('sportsmen/', include('sportsmen.urls')),
]
