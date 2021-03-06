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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from aboutme import views as aboutme_views
from projects import views as project_views
from blog import views as blog_views
from info import views as info_views
from shop import views as shop_views
from photologue.sitemaps import GallerySitemap, PhotoSitemap
#from photologue_custom.views import MyGalleryDetailView

sitemaps = {'photologue_galleries': GallerySitemap,
	    'photologue_photos': PhotoSitemap,
	}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', aboutme_views.view_home, name='home'),
    url(r'^about-me', aboutme_views.view_about_me, name="about_me"),
   # url(r'^gallery', project_views.view_showcase, name="gallery"),
   # url(r'^gallery/(?P<slug>[\-\d\w]+)$', MyGalleryDetailView.as_view(), name="gallery"),
    url(r'^how-to-order', project_views.view_commission, name='commission'),
    url(r'^blog', blog_views.view_blog, name='blog'),
    url(r'^contact-mark', aboutme_views.view_contact_me, name='contact-me'),
    url(r'^links', info_views.view_links, name='links'),
    url(r'^buy-a-necklace', shop_views.view_buy_a_necklace, name='buy-a-necklace'),
    url(r'^view-cart', shop_views.view_cart, name='view-cart'),
]

urlpatterns += [
#	url(r'^gallery/', include('photologue_custom.urls', namespace='photologue_custom')),
#	url(r'^photologue/', include('photologue.urls', namespace='photologue')),
	url(r'^my-', include('photologue.urls', namespace='photologue')),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#NB this last bit is for serving uploaded files on the development server (see https://docs.djangoproject.com/en/1.9/)


