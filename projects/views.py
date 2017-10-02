from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def view_showcase(request):
	#return HttpResponse()
	return render(request, 'showcase.html')

def view_commission(request):
	return render(request, 'commissions.html')
