from django.db import models

from taggit.managers import TaggableManager

from photologue.models import Gallery


class GalleryExtended(models.Model):

	# Link back to Photologue's Gallery model.
	gallery = models.OneToOneField(Gallery, related_name='extended')

	# This is the important bit - where we add in the tags.
	tags = TaggableManager(blank=True)

	# Boilderplate code to make a prettier display in the admin interface.
	class Meta:
	   verbose_name = u'Extra fields'
	   verbose_name_plural = u'Extra fields'

	def __str__(self):
	   return self.gallery.title

	def get_absolute_url(self):
  	   return reverse('gallery', args=[self.gallery.slug])

class MyGallery(Gallery):

	class Meta:
		proxy = True
	
	def get_absolute_url(self):
	   return reverse('gallery', args=[self.slug])
