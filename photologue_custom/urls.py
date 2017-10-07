from django.conf.urls import url

from photologue_custom.views import MyGalleryDetailView
from .views import PhotoJSONListView

urlpatterns = [
	url(r'^(?P<slug>[\-\d\w]+)/$', MyGalleryDetailView.as_view(), name="gallery"),
	url(r'^photolist/$',PhotoJSONListView.as_view(),name='photolgue_custom-photo-json-list'),
#	url(r'^doorknobs-gallery(?P<slug>)/$', SpecificGalleryDetailView.as_view(),
#	name='test')
]
