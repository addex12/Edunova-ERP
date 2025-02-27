from flask import Blueprint, request, jsonify
from app.models import Student, Teacher
from app import db
import pandas as pd
from io import StringIO

data_bp = Blueprint('data', __name__, url_prefix='/api/data')

@data_bp.route('/import/students', methods=['POST'])
@role_required(['admin'])
def import_students():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        df = pd.read_csv(StringIO(file.read().decode('utf-8')))
        for _, row in df.iterrows():
            student = Student(
                admission_number=row['admission_number'],
                user=User(
                    username=row['username'],
                    email=row['email'],
                    password_hash=generate_password_hash(str(row['dob'])),  # Temp password
                    role='student'
                )
            )
            db.session.add(student)
        db.session.commit()
        return jsonify({'imported': len(df)}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
