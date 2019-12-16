"""ecommerce URL Configuration

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
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from products.views import product_list_view, product_detail_view
from .views import home_page, contact_page, about_page, login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('contact/', contact_page),
    path('about/', about_page),
    path('login/', login_page),
    path('register/', register_page),
    path('product/', product_list_view, name='list'),
    path('product/<int:pk>/', product_detail_view, name='detail'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
