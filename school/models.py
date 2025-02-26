# school/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    user_type = models.CharField(max_length=50)  # "parent", "student", "teacher", etc.

    def __str__(self):
        return self.username

class ReportCard(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    grades = models.JSONField()  # Flexible grading structure
    report_template = models.TextField()

    def __str__(self):
        return f"Report Card for {self.student}"

# Add more models based on requirements
