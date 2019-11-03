from django.conf.urls import re_path, include
from .views import all_ammonites

urlpatterns = [
    re_path(r'^$', all_ammonites, name='fossils'),
]