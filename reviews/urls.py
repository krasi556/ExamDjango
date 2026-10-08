from django.urls import path, include

from reviews import views

app_name = 'reviews'

urlpatterns = [

    path('show-employees-reviews/', views.show_employees_for_review, name='show-employees-reviews'),

    path('employee-reviews-<int:employee_id>/', include([
        path('', views.current_employee_reviews, name='current-employee-reviews'),
        path('create/', views.leave_review, name='leave-review'),
    ])),
    path('review-<int:review_id>/', include([
        path('edit/', views.edit_review, name='edit-review'),
        path('delete/', views.delete_review, name='delete-review')
    ]))

]
