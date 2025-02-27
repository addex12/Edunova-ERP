from flask import Blueprint, jsonify
from app.models import User, Student, Teacher
from app.middleware.auth import role_required
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin_bp.route('/users', methods=['GET'])
@role_required(['admin'])
def get_all_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'role': u.role,
        'created_at': u.created_at.isoformat(),
        'profile': {
            'admission_number': u.student_profile.admission_number if u.role == 'student' else None,
            'employee_id': u.teacher_profile.employee_id if u.role == 'teacher' else None
        }
    } for u in users]), 200

@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
@role_required(['admin'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200
