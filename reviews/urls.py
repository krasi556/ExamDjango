from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [

    path('show-employees-reviews/', views.show_employees_for_review, name='show-employees-reviews'),
    path('review-employee-<int:employee_id>/',views.leave_review,name='leave-review')

]
