
from django.conf.urls import patterns, url
from . import views as lists_views

# app_name = 'lists'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', lists_views.view_list, name='view_list'),
    url(r'^(?P<pk>[0-9]+)/add_item$', lists_views.add_item, name='add_item'),
    url(r'^new$', lists_views.new_list, name='new_list'),
]
