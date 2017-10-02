from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_blog(request):
  # return HttpResponse()
   return render(request, 'blog.html')
