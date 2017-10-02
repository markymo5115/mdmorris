from django.shortcuts import render

# Create your views here.

def view_buy_a_necklace(request):
	return render(request, 'buy_a_necklace.html')

def view_cart(request):
	return render(request, 'cart.html')
