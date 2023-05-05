from django.urls import path
from .views import home,get,create
urlpatterns = [
    path('',home),
    path('get-student',get),
    path('student',create)]
