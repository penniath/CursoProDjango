from django.shortcuts import render
from .models import Event, Category

def index(request):
	events = Event.objects.all().order_by('-created')[:6]
	categories = Category.objects.all()
	return render(request, 'index.html', 
		{'events': events, 'categories': categories})
