"""mdmorris URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from aboutme import views as aboutme_views
from projects import views as project_views
from blog import views as blog_views
from info import views as info_views
from shop import views as shop_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', aboutme_views.view_home, name='home'),
    url(r'^about-me', aboutme_views.view_about_me, name="about_me"),
    url(r'^gallery', project_views.view_showcase, name="gallery"),
    url(r'^how-to-order', project_views.view_commission, name='commission'),
    url(r'^blog', blog_views.view_blog, name='blog'),
    url(r'^contact-mark', aboutme_views.view_contact_me, name='contact-me'),
    url(r'^links', info_views.view_links, name='links'),
    url(r'^buy-a-necklace', shop_views.view_buy_a_necklace, name='buy-a-necklace'),
    url(r'^view-cart', shop_views.view_cart, name='view-cart'),
]
