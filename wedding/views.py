from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def home(request):
	return render(request, 'home.html')

def bride(request):
	return render(request, 'bride.html')

def reception(request):
	return render(request, 'reception.html')

def ceremony(request):
	return render(request, 'ceremony.html')

def groom(request):
	return render(request, 'groom.html')