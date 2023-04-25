
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name='index'),
    path("layout/", views.layout, name='layout'),
    path("hostel/", views.hostel, name='hostel'),
] 


'''path("administration/", views.administration, name="administration"),
path("admission-criteria/", views.admission_criteria, name="admission-criteria"),
path("admission-procedure/", views.admission_procedure, name="admission-procedure"),
path("contact/", views.contact, name="contact"),'''
