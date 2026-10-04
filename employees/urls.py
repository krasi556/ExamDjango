
from django.urls import path

from employees import views

urlpatterns = [

                  path('', views.current_employees, name='current-employees')

              ]
