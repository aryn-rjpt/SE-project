from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/home.html')

def layout(request):
    return render(request, 'home/layout.html')