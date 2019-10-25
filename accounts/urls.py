from django.urls import path, include, reverse, re_path
from . import urls_reset
from .views import index, register, profile, logout, login


urlpatterns = [
    re_path(r'^register/$', register, name='register'),
    re_path(r'^profile/$', profile, name='profile'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^login/$', login, name='login'),
    re_path(r'^password-reset/', include(urls_reset)),
]
