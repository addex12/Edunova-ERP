
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('teacher', 'Teacher'),
        ('head', 'Head of School'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=20, unique=True)
    class_grade = models.CharField(max_length=10)
    parent = models.ForeignKey('Parent', on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField()

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='parents')

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField('Subject')
    qualification = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    
class GradingScale(models.Model):
    name = models.CharField(max_length=50)
    min_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    max_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    grade = models.CharField(max_length=2)
    
class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=9)
    date_generated = models.DateTimeField(auto_now_add=True)
    template = models.ForeignKey('ReportTemplate', on_delete=models.PROTECT)
    
class ReportTemplate(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()  # HTML template with placeholders
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    term = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=9)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    date_recorded = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student', 'subject', 'term', 'academic_year']

