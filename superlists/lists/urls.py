
# /lists/urls.py

from django.conf.urls import patterns, url
from . import views as lists_views

app_name = 'lists'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', lists_views.view_list, name='view_list'),
    url(r'^new$', lists_views.new_list, name='new_list'),
    url(r'^users/(.+)/$', lists_views.my_lists, name='my_lists'),
    url(r'^(?P<pk>[0-9]+)/share$', lists_views.share_list, name='share_list'),
]
