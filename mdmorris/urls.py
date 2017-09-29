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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', admin.site.urls),
    url(r'^about-me', aboutme_views.view_about_me, name="about_me"),
    url(r'^gallery', admin.site.urls),
    url(r'^how-to-order', admin.site.urls),
    url(r'^blog', admin.site.urls),
    url(r'^contact-mark', admin.site.urls),
    url(r'^links', admin.site.urls),
    url(r'^buy-a-necklace', admin.site.urls),
    url(r'^view-cart', admin.site.urls),
]
