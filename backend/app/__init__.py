from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_admin import Admin as FlaskAdmin
from config import Config

# Initialize extensions first
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
admin_panel = FlaskAdmin(name='Edunova ERP', template_mode='bootstrap3')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    admin_panel.init_app(app)

    # Import models after db initialization
    from app.models import User, ReportTemplate

    # Import views after models are available
    from app.admin.views import (
        DashboardView,
        UserAdminView,
        ReportAdminView,
        DataImportView
    )

    # Add admin views
    admin_panel.add_view(DashboardView(name='Dashboard', endpoint='dashboard'))
    admin_panel.add_view(UserAdminView(User, db.session, name='Users'))
    admin_panel.add_view(ReportAdminView(ReportTemplate, db.session, name='Reports'))
    admin_panel.add_view(DataImportView(name='Data Import', endpoint='data-import'))

    return app
