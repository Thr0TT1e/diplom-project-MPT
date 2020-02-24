from django.shortcuts import render
from .models import CardProduct

# Create your views here.


def index(request):
	return render(request, 'general/index.html', {})
