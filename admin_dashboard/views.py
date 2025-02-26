from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AdminDashboard
from .forms import AdminDashboardForm

@login_required
def admin_dashboards(request):
    dashboards = AdminDashboard.objects.all()
    return render(request, 'admin_dashboard.html', {'dashboards': dashboards})

@login_required
def create_admin_dashboard(request):
    if request.method == 'POST':
        form = AdminDashboardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboards')
    else:
        form = AdminDashboardForm()
    return render(request, 'create_admin_dashboard.html', {'form': form})
