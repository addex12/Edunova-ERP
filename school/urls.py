# school/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('report_card/', views.report_card, name='report_card'),
    # Add more paths as needed
]
