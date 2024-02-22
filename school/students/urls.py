from django.urls import path
from . import views

urlpatterns = [

    path('', views.school),
    path('students/', views.students)
]