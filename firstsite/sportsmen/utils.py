from django.db.models import Count
from .models import Sports

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        sports = Sports.objects.annotate(cnt=Count('sportsman')).filter(cnt__gt=0)
        context['sports'] = sports
        if 'sport_selected' not in context:
            context['sport_selected'] = 0
        return context
