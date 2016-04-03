
from django.conf.urls import patterns, include, url
from django.contrib import admin

from lists import views as lists_views

urlpatterns = [
    url(r'^$', lists_views.home_page, name='home'),
    url(r'^lists/(?P<pk>[0-9]+)/$', lists_views.view_list, name='view_list'),
    url(r'^lists/(?P<pk>[0-9]+)/add_item$', lists_views.add_item, name='add_item'),
    url(r'^lists/new$', lists_views.new_list, name='new_list'),

    # url(r'^admin/', admin.site.urls),
]
