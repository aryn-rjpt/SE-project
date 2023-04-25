from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'home/home.html')

def layout(request):
    return render(request, 'home/layout.html')

def hostel(request):
    return render(request, 'home/hostel.html')

# def administration(request):
#     return render(request, 'home/administration.html')

# def admission_criteria(request):
#     return render(request, 'home/admission_criteria.html')

# def admission_procedure(request):
#     return render(request, 'home/admission_procedure.html')

# def contact(request):
#     return render(request, 'home/contact.html')
