from django.urls import path
from . import views

urlpatterns = [
    path('parents/', views.ParentList.as_view(), name='parent-list'),
    path('students/', views.StudentList.as_view(), name='student-list'),
    path('teachers/', views.TeacherList.as_view(), name='teacher-list'),
]
