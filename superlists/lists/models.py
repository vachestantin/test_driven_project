
# /lists/models.py

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('lists:view_list', args=[self.id])

    def __str__(self):
        return '{}번째 리스트'.format(self.pk)


class Item(models.Model):
    text = models.TextField(default='', unique=False)
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
