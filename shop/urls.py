"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse, include, re_path
from accounts import urls as urls_accounts
from products import urls as urls_ammonites
from cart import urls as urls_cart
from products.views import all_products
from django.views import static
from django.conf.urls.static import static, serve

from .settings import MEDIA_ROOT
from django.conf import settings
from home.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('ammonites/', include(urls_ammonites)),
    path('accounts/', include(urls_accounts)),
    path('cart/', include(urls_cart)),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
