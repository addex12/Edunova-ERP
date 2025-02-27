from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')

@dashboard_bp.route('/', methods=['GET'])
@jwt_required()
def get_dashboard():
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    dashboard_data = {
        'username': user.username,
        'role': user.role,
        'created_at': user.created_at.isoformat(),
        'profile': {}
    }
    
    if user.role == 'student':
        dashboard_data['profile'] = {
            'admission_number': user.student_profile.admission_number,
            'grades': [{
                'subject': grade.subject,
                'marks': grade.marks
            } for grade in user.student_profile.grades]
        }
    elif user.role == 'teacher':
        dashboard_data['profile'] = {
            'employee_id': user.teacher_profile.employee_id,
            'qualification': user.teacher_profile.qualification
        }
    
    return jsonify(dashboard_data), 200
