from django.db import models
from django.contrib.auth.models import AbstractUser

class AdminDashboard(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dashboard_name = models.CharField(max_length=255)
    dashboard_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dashboard_namefrom django.db import models

# Create your models here.
