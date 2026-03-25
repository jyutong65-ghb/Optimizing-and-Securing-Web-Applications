from django import forms
from django.core.exceptions import ValidationError
from .models import Sportsman, Sports

class AddArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sport'].empty_label = 'Choose sport'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('The length of the title is more than 200 characters.')
        return title

    class Meta:
        model = Sportsman
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'sport']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 12, 'class': 'form-input'}),
        }
