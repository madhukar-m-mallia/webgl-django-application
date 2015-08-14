from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'auth/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'auth/logout.html'}),
]