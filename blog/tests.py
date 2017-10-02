from django.test import TestCase

# Create your tests here.
class TestBlogViews(TestCase):

	def test_blog_uses_blog_template(self):
		response = self.client.get('/blog')
		self.assertTemplateUsed(response, 'blog.html')

	def test_blog_template_has_correct_title(self):
		response  = self.client.get('/blog')
		self.assertContains(response,
			"<title>MDMorris' Blog</title>",
			html=True)

