
from django.conf.urls import patterns, include, url
from django.contrib import admin

from lists import views as lists_views
from lists.urls import urlpatterns as lists_urls
from accounts.urls import urlpatterns as accounts_urls


urlpatterns = [
    url(r'^$', lists_views.home_page, name='home'),
    url(r'^lists/', include(lists_urls, namespace='lists')),
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),

    url(r'^admin/', admin.site.urls),
]
