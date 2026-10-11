from django.urls import path

from core import views

app_name = 'core'
urlpatterns = [
    path('', views.load_main_page, name='load-main-page'),
    path('redirect-home/', views.redirect_to_main_page, name='redirect-home'),
    path('about-us/', views.load_about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact-us')
]
