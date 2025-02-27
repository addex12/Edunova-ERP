from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SelectField,
    FileField,
    SubmitField,
    TextAreaField
)
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    role = SelectField('Role', choices=[
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('admin', 'Admin')
    ], validators=[DataRequired()])
    admission_number = StringField('Admission Number')
    employee_id = StringField('Employee ID')
    submit = SubmitField('Register')

class DataImportForm(FlaskForm):
    file = FileField('CSV File', validators=[DataRequired()])
    submit = SubmitField('Import Data')

class SQLQueryForm(FlaskForm):
    query = TextAreaField('SQL Query', validators=[DataRequired()])
    submit = SubmitField('Execute')
