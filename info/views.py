from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def view_links(request):
	return render(request, 'links.html')
