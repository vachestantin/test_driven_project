
from django.conf.urls import patterns, url
from . import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    url(r'^login$', accounts_views.persona_login, name='persona_login'),
]
