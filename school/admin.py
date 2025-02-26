# school/admin.py

from django.contrib import admin
from .models import User, ReportCard

admin.site.register(User)
admin.site.register(ReportCard)
