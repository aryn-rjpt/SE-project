
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name='index'),
    path("layout/", views.layout, name='layout'),
    path("campus/", views.campus, name='campus'),
    path("hostel/", views.hostel, name='hostel'),
    path("canteen/", views.canteen, name='canteen'),
    path("auditorium/", views.auditorium, name='auditorium'),
    path("classroom/", views.classroom, name='classroom'),
    path("courses/", views.courses, name='courses'),
    path("syllabus/", views.syllabus, name='syllabus'),
    path("director/", views.director, name='director'),
    path("alumni/", views.alumni, name='alumni'),
    path("mission/", views.mission, name='mission'),
    path("vision/", views.vision, name='vision'),
    path("exhibition/", views.exhibition, name='exhibition'),
    path("events/", views.events, name='events'),

] 


