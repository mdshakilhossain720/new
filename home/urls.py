from django.urls import path
from . import views

urlpatterns = [
    path('regestion/',views.StudentView,name='form'),
]
