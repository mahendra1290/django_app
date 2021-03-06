"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url

from django.contrib import admin
from products.views import contact_view, about_view, product_form_view, dynamic_url_routing

urlpatterns = [
    url('products/', include('products.urls')),
    url('contact/', contact_view, name='contact'),
    url('about/', about_view, name='about'),
    url(r'^produc/(?P<id>\d+)/', dynamic_url_routing, name='dynamic_routing'),
    url('produc/form/', product_form_view, name='product_form'),

    url('admin/', admin.site.urls),
]
