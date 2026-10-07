from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [

    path('leave-review/', views.leave_review, name='leave-review')

]
