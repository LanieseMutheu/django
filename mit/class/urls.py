from django.urls import path
from . import views


urlpatterns = [

    path('', views.home),
    path('product/', views.product),
    path('students/',views.students),
    path('teachers/', views.teachers),
    path('insert_students',views.insert_students)
]