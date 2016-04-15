
# /accounts/urls.py

from django.conf.urls import patterns, url
from django.contrib.auth.views import logout
from . import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    url(r'^login$', accounts_views.persona_login, name='persona_login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
