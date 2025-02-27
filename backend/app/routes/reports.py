from flask import Blueprint, request, jsonify
from app.models import ReportTemplate, StudentReport
from app.middleware.auth import role_required
from app import db

report_bp = Blueprint('report', __name__, url_prefix='/api/reports')

@report_bp.route('/templates', methods=['POST'])
@role_required(['admin', 'teacher'])
def create_template():
    data = request.json
    new_template = ReportTemplate(
        name=data['name'],
        template_html=data['template_html'],
        school_id=data.get('school_id')
    )
    db.session.add(new_template)
    db.session.commit()
    return jsonify({'id': new_template.id}), 201

@report_bp.route('/generate/<int:student_id>', methods=['POST'])
@role_required(['admin', 'teacher'])
def generate_report(student_id):
    template = ReportTemplate.query.get(request.json['template_id'])
    student = Student.query.get(student_id)
    
    rendered_html = template.template_html.format(
        student_name=student.user.username,
        grades={grade.subject: grade.marks for grade in student.grades}
    )
    
    new_report = StudentReport(
        student_id=student_id,
        template_id=template.id,
        generated_html=rendered_html
    )
    db.session.add(new_report)
    db.session.commit()
    return jsonify({'report_id': new_report.id}), 201
