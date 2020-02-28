from django.shortcuts import render
from .models import CardProduct

# Create your views here.


def index(request):
	# main_content =
	return render(request, 'general/index.html', {})
