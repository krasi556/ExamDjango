from django.urls import path, include

from employees import views

app_name = 'employees'

urlpatterns = [

    path('', views.CurrentEmployeeListView.as_view(), name='current-employees'),
    path('join-us/', views.CreateEmployeeView.as_view(), name='create-profile'),
    path('employee-<int:pk>/', include([
        path('', views.FocusedEmployee.as_view(), name='focused-employee'),
        path('edit/', views.EditEmployeeView.as_view(), name='edit'),
        path('delete/', views.DeleteEmployeeView.as_view(), name='delete'),
        path('hire/', views.HireEmployee.as_view(), name='hire-employee'),
        path('edit-review/',views.LeaveAReview.as_view(),name='edit-employee-review')

    ])),
    path('join-us/', include([
        path('done/', views.new_job, name='new-job'),
        path('wait/', views.you_would_miss_out, name='you-would-miss-out')
    ])),
    path('skills-menu/', views.show_skills, name='skills-menu'),
    path('add-skill/', views.AddSkill.as_view(), name='add-skill'),

]
