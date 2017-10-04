from django.conf.urls import *

from photologue.views import GalleryListView

urlpatterns = [
	url(r'^gallerylist/$', 
	GalleryListView.as_view(paginate_by=10),
	name='phologue_custom-gallery-list'),
]
