from django.urls import path, include

from employees import views

app_name = 'employees'

urlpatterns = [

    path('', views.current_employees, name='current-employees'),
    path('join-us/', views.create_profile, name='create-profile'),
    path('employee-<int:pk>/', include([
        path('', views.focused_employee, name='focused-employee'),
        path('edit/', views.edit_employee, name='edit'),
        path('delete/', views.DeleteEmployeeView.as_view(), name='delete'),
        path('hire/', views.hire_employee, name='hire-employee')

    ])),
    path('join-us/', include([
        path('done/', views.new_job, name='new-job'),
        path('wait/', views.you_would_miss_out, name='you-would-miss-out')
    ])),
    path('skills-menu/', views.show_skills, name='skills-menu'),
    path('add-skill/', views.add_skill, name='add-skill'),

]
