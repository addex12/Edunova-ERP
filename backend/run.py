
from flask import Flask
from app.models import db
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URL'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the db with the Flask app
db.init_app(app)

with app.app_context():
    db.create_all()  # Create database tables

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

