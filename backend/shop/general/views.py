from django.shortcuts import render
from .models import CardProduct

# Create your views here.


def index(request):
	# main_content =
	return render(request, 'general/main.html', {})

def lk_info(request):
	return render(request, 'general/lk_info.html', {})

def lk_orders(request):
	return render(request, 'general/lk_orders.html', {})
