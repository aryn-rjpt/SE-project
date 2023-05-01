from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'home/home.html')

def layout(request):
    return render(request, 'home/layout.html')

def campus(request):
    return render(request, 'home/campus.html')

def hostel(request):
    return render(request, 'home/hostel.html')

def canteen(request):
    return render(request, 'home/canteen.html')

def auditorium(request):
    return render(request, 'home/auditorium.html')

def classroom(request):
    return render(request, 'home/classroom.html')

def courses(request):
    return render(request, 'home/courses.html')

def syllabus(request):
    return render(request, 'home/syllabus.html')

def director(request):
    return render(request, 'home/director.html')

def alumni(request):
    return render(request, 'home/alumni.html')

def mission(request):
    return render(request, 'home/mission.html')

def vision(request):
    return render(request, 'home/vision.html')

def exhibition(request):
    return render(request, 'home/exhibition.html')

def events(request):
    return render(request, 'home/events.html')

def timetable(request):
    return render(request, 'home/timetable.html')
