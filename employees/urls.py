from django.urls import path, include

from employees import views

app_name = 'employees'

urlpatterns = [

    path('', views.current_employees, name='current-employees'),
    path('join-us/', views.create_profile, name='create-profile'),
    path('employee-<int:employee_id>/', include([
        path('', views.focused_employee, name='focused-employee'),
        path('edit/', views.edit_employee, name='edit'),
        path('delete/',views.delete_employee,name='delete')

    ])),

]
