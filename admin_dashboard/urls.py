from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboards, name='admin_dashboards'),
    path('create/', views.create_admin_dashboard, name='create_admin_dashboard'),
]
