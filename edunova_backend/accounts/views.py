from rest_framework import generics
from .models import Parent, Student, Teacher
from .serializers import ParentSerializer, StudentSerializer, TeacherSerializer

class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
