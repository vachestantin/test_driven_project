
from django.conf.urls import url
from accounts import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    url(r'^login$', accounts_views.login, name='login'),
    url(r'^logout$', accounts_views.logout, name='logout'),
]
