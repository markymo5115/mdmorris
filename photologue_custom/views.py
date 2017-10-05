from django.shortcuts import render

from photologue.views import PhotoListView, GalleryDetailView

from braces.views import JSONResponseMixin

class PhotoJSONListView(JSONResponseMixin, PhotoListView):

	def render_to_response(self, context, **response_kwargs):
		return self.render_json_object_response(context['object_list'], **response_kwargs)

#class SpecificGalleryDetailView(GalleryDetailView):
#	queryset = GalleryDetailView.queryset.filter(slug='doorknobs')

