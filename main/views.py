from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
def homepage(request):
    return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")
'''

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def cv(request):
    return render(request, 'main/cv.html')
