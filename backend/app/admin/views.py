# In app/admin/views.py
from flask import request, redirect, url_for
from flask_admin.base import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from wtforms import PasswordField, validators  # Added validators import
from app.models import User, ReportTemplate
import pandas as pd
from io import StringIO
from datetime import datetime

class DashboardView(BaseView):
    @expose('/')
    def index(self):
        stats = {
            'total_users': User.query.count(),
            'total_reports': ReportTemplate.query.count(),
            'active_users': User.query.filter(User.role != 'inactive').count()
        }
        return self.render('admin/dashboard.html', stats=stats)

class UserAdminView(ModelView):
    column_list = ['username', 'email', 'role', 'created_at']
    column_searchable_list = ['username', 'email']
    column_filters = ['role']
    form_columns = ['username', 'email', 'role', 'password']
    column_exclude_list = ['password_hash']

    # Corrected form_extra_fields definition
    form_extra_fields = {
        'password': PasswordField(
            'Password',
            validators=[
                validators.DataRequired(),
                validators.Length(min=8, message="Password must be at least 8 characters")
            ]
        )
    }

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password_hash = generate_password_hash(form.password.data)

class ReportAdminView(ModelView):
    column_list = ['name', 'created_at', 'modified_at']
    form_columns = ['name', 'template_html']
    column_searchable_list = ['name']

    form_args = {
        'name': {
            'validators': [validators.DataRequired()]
        }
    }

    def on_model_change(self, form, model, is_created):
        model.modified_at = datetime.utcnow()

class DataImportView(BaseView):
    @expose('/', methods=('GET', 'POST'))
    def index(self):
        if request.method == 'POST':
            file = request.files.get('csv_file')
            if file and file.filename.endswith('.csv'):
                try:
                    df = pd.read_csv(StringIO(file.read().decode('utf-8')))
                    # Add your data import logic here
                    return redirect(url_for('admin.index'))
                except Exception as e:
                    return self.render('admin/data_import.html', error=str(e))
            return self.render('admin/data_import.html', error="Invalid file format")
        return self.render('admin/data_import.html')
