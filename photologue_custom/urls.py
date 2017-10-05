from django.conf.urls import *

from photologue.views import GalleryListView
from .views import PhotoJSONListView

urlpatterns = [
	url(r'^gallerylist/$', 
	GalleryListView.as_view(paginate_by=4),
	name='phologue_custom-gallery-list'),
	url(r'^photolist/$',
	PhotoJSONListView.as_view(),
	name='photolgue_custom-photo-json-list'),
#	url(r'^doorknobs-gallery(?P<slug>)/$', SpecificGalleryDetailView.as_view(),
#	name='test')
]
