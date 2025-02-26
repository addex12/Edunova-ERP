from django import forms
from .models import AdminDashboard

class AdminDashboardForm(forms.ModelForm):
    class Meta:
        model = AdminDashboard
        fields = ('dashboard_name', 'dashboard_description')
