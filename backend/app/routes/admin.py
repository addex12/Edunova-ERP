from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Feature
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def admin_dashboard():
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin':
        return jsonify({'error': 'Unauthorized access'}), 403
    
    # Fetch all users for the admin dashboard
    users = User.query.all()
    users_data = [{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role,
        'created_at': user.created_at.isoformat()
    } for user in users]
    
    # Fetch all registered features
    features = Feature.query.all()
    features_data = [{
        'id': feature.id,
        'name': feature.name,
        'description': feature.description,
        'is_active': feature.is_active
    } for feature in features]
    
    return jsonify({
        'users': users_data,
        'features': features_data
    }), 200
@admin_bp.route('/features/<int:feature_id>/toggle', methods=['PUT'])
@jwt_required()
def toggle_feature(feature_id):
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin':
        return jsonify({'error': 'Unauthorized access'}), 403
    
    feature = Feature.query.get_or_404(feature_id)
    feature.is_active = not feature.is_active
    db.session.commit()
    
    return jsonify({'message': 'Feature toggled successfully'}), 200    
    db.session.add(new_feature)
    db.session.commit()
    
    return jsonify({'message': 'Feature added successfully'}), 201
