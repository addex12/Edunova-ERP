from flask import Flask
from app.config import Config
from app.models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()  # Create database tables

if __name__ == "__main__":
    app.run(debug=True)
