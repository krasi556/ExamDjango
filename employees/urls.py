from django.urls import path

from employees import views

urlpatterns = [

    path('', views.current_employees, name='current-employees'),
    path('employee-<int:employee_id>/', views.focused_employee, name = 'focused-employee')
]
