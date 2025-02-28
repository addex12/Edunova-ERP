# Edunova ERP - School Management System

A comprehensive web-based School Management System built with Flask and React, designed for educational institutions.

## 🚀 Features

### User Management
- Role-based access control (Admin, Teacher, Student, Parent)
- JWT-based secure authentication
- Password hashing for enhanced security

### Admin Dashboard
- System statistics and monitoring
- Complete user management (CRUD)
- Report template management

### Data Management
- CSV bulk import for students and teachers
- Report and data export functionality

### Reporting
- Customizable report card templates
- Dynamic student data placeholders

### Monitoring
- Real-time system metrics (CPU, memory, disk)
- Audit-ready activity logging

## 🛠️ Tech Stack

### Backend
- Flask (Python)
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Admin
- Flask-JWT-Extended
- PostgreSQL

### Frontend
- React.js
- Material-UI
- Axios

### Tools
- Alembic
- Pandas
- psutil

## 📋 Prerequisites

```bash
# Python 3.10+
sudo apt install python3.10

# PostgreSQL
sudo apt install postgresql postgresql-contrib

# Node.js
sudo apt install nodejs npm
```

## ⚙️ Installation

### Backend Setup
```bash
# Clone repository
git clone https://github.com/yourusername/edunova-erp.git
cd edunova-erp/backend

# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Database setup
sudo -u postgres createdb edunova

# Environment configuration
DATABASE_URL=postgresql://edunova:edunova@localhost/edunova

# Migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Start server
flask run
```

### Frontend Setup
```bash
cd ../frontend
npm install
npm start
```

Access the application at: `http://localhost:3000`

## 🔧 Usage

### Admin Portal
Access at: `http://localhost:5000/admin`
- Dashboard overview
- User management
- Report management
- Data import/export

### API Endpoints

#### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User authentication

#### Users
- `GET /api/users` - List users
- `POST /api/users` - Create user
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user

#### Reports
- `GET /api/reports` - List reports
- `POST /api/reports` - Create report
- `PUT /api/reports/<id>` - Update report
- `DELETE /api/reports/<id>` - Delete report

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 📞 Contact

Your Name
- Email: your.email@example.com
- GitHub: [@addex12](https://github.com/addex12)
