
from django.core.urlresolvers import reverse
from django.db import models

class List(models.Model):
    def get_absolute_url(self):
        return reverse('lists:view_list', args=[self.id])

    def __str__(self):
        return '{}번째 리스트'.format(self.pk)


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    def __str__(self):
        return '{}번째 아이템: {}'.format(self.pk, self.text)
