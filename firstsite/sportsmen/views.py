from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Sportsman, Sports
from .forms import AddArticleForm
from .utils import DataMixin

menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_article'},
    {'title': 'Contacts', 'url_name': 'contact'},
    {'title': 'Sign in', 'url_name': 'login'},
]

def about(request):
    return render(request, 'sportsmen/about.html', {
        'menu': menu,
        'title': 'About',
        'sport_selected': 0,
    })

def contacts(request):
    return HttpResponse('<h1>Contact information</h1>')

def login(request):
    return HttpResponse('<h1>Log in</h1>')

def contact(request):
    return render(request, 'sportsmen/contact.html', {
        'menu': menu,
        'title': 'Contacts',
        'sport_selected': 0,
    })

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404 - Page Not Found</h1>')

# ---------- Class-based views with DataMixin ----------
class SportsmenHome(DataMixin, ListView):
    model = Sportsman
    template_name = 'sportsmen/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Sportsman.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main page')
        return {**context, **c_def}

class SportsmenSport(DataMixin, ListView):
    model = Sportsman
    template_name = 'sportsmen/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return Sportsman.objects.filter(
            sport__slug=self.kwargs['sport_slug'],
            is_published=True
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sport = Sports.objects.get(slug=self.kwargs['sport_slug'])
        c_def = self.get_user_context(
            title=f'Sport - {sport.name}',
            sport_selected=sport.pk
        )
        return {**context, **c_def}

class ShowPost(DataMixin, DetailView):
    model = Sportsman
    template_name = 'sportsmen/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return {**context, **c_def}

class AddArticle(DataMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'sportsmen/addarticle.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add article')
        return {**context, **c_def}
