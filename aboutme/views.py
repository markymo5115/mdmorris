from django.shortcuts import render

# Create your views here.

def view_home(request):
	return render(request,'home.html')

def view_about_me(request):
	return render(request, 'aboutme.html')

def view_contact_me(request):
	return render(request, 'contactme.html')
