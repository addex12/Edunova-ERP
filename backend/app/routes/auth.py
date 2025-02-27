from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.models import User, Student, Teacher
from app import db

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET'])
def home():
    return render_template('dashboard.html')
    
@auth_bp.route('/register', methods=['POST'])
def register():
    # Get JSON data from the request
    data = request.get_json()

    # Validate required fields
    required_fields = ['username', 'email', 'password', 'role']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if username or email already exists
    existing_user = User.query.filter(
        (User.username == data['username']) | 
        (User.email == data['email'])
    ).first()

    if existing_user:
        conflict_field = 'username' if existing_user.username == data['username'] else 'email'
        return jsonify({
            'error': f'{conflict_field.capitalize()} already exists',
            'field': conflict_field
        }), 409

    try:
        # Create a new user
        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=generate_password_hash(data['password']),
            role=data['role']
        )
        db.session.add(new_user)
        db.session.flush()  # Assigns an ID to the user without committing

        # Create role-specific profile
        if data['role'] == 'student':
            if not data.get('admission_number'):
                return jsonify({'error': 'Admission number is required for students'}), 400
            student = Student(
                user_id=new_user.id,
                admission_number=data['admission_number']
            )
            db.session.add(student)
        elif data['role'] == 'teacher':
            if not data.get('employee_id'):
                return jsonify({'error': 'Employee ID is required for teachers'}), 400
            teacher = Teacher(
                user_id=new_user.id,
                employee_id=data['employee_id']
            )
            db.session.add(teacher)

        # Commit changes to the database
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        # Rollback in case of error
        db.session.rollback()
        return jsonify({'error': 'Registration failed', 'details': str(e)}), 500
