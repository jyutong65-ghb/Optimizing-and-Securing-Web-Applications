from django.db import models
from django.urls import reverse

class Sportsman(models.Model):
    title = models.CharField(max_length=255, verbose_name='Article title')
    content = models.TextField(blank=True, verbose_name='Article content')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Time of last modification')
    is_published = models.BooleanField(default=True, verbose_name='Publication')
    sport = models.ForeignKey('Sports', on_delete=models.PROTECT, null=True, verbose_name='Sports')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Sports news'
        verbose_name_plural = 'Sports news'
        ordering = ['time_create', 'title']

class Sports(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='The name of the sport')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sport', kwargs={'sport_id': self.pk})

    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'
        ordering = ['name']
