
from django.db import models

class List(models.Model):
    pass

    def __str__(self):
        return '{}번째 리스트'.format(self.pk)


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    def __str__(self):
        return '{}번째 아이템: {}'.format(self.pk, self.text)
