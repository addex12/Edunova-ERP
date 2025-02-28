Edunova ERP

Edunova ERP is a full-featured web-based School Management System built using Flask (Python) for the backend and React for the frontend. It provides tools for managing students, teachers, parents, and administrative tasks in an educational institution.
Features

    User Management:

        Role-based access control (Admin, Teacher, Student, Parent).

        Secure authentication with JWT.

        Password hashing for security.

    Admin Dashboard:

        System statistics and monitoring.

        User management (CRUD operations).

        Report template management.

    Data Import/Export:

        Bulk import of students and teachers via CSV.

        Export functionality for reports and data.

    Report Generation:

        Customizable report card templates.

        Dynamic placeholders for student data.

    System Monitoring:

        Real-time system health metrics (CPU, memory, disk usage).

        Activity logs for auditing.

Technologies Used

    Backend:

        Flask (Python)

        Flask-SQLAlchemy (ORM)

        Flask-Migrate (Database migrations)

        Flask-Admin (Admin interface)

        Flask-JWT-Extended (Authentication)

        PostgreSQL (Database)

    Frontend:

        React.js

        Material-UI (UI components)

        Axios (HTTP requests)

    Other Tools:

        Alembic (Database migrations)

        Pandas (Data processing for CSV imports)

        psutil (System monitoring)

Setup Instructions
Prerequisites

    Python 3.10+:
    bash
    Copy

    sudo apt install python3.10

    PostgreSQL:
    bash
    Copy

    sudo apt install postgresql postgresql-contrib

    Node.js (for frontend):
    bash
    Copy

    sudo apt install nodejs npm

Backend Setup

    Clone the repository:
    bash
    Copy

    git clone https://github.com/yourusername/edunova-erp.git
    cd edunova-erp/backend

    Create a virtual environment:
    bash
    Copy

    python3 -m venv venv
    source venv/bin/activate

    Install dependencies:
    bash
    Copy

    pip install -r requirements.txt

    Set up the database:

        Create a PostgreSQL database:
        bash
        Copy

        sudo -u postgres createdb edunova

        Update the database URL in .env:
        Copy

        DATABASE_URL=postgresql://edunova:edunova@localhost/edunova

    Run migrations:
    bash
    Copy

    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

    Start the backend server:
    bash
    Copy

    flask run

Frontend Setup

    Navigate to the frontend directory:
    bash
    Copy

    cd ../frontend

    Install dependencies:
    bash
    Copy

    npm install

    Start the development server:
    bash
    Copy

    npm start

    Access the frontend at:
    Copy

    http://localhost:3000

Usage
Admin Interface

Access the admin interface at:
Copy

http://localhost:5000/admin

    Dashboard: View system statistics and health metrics.

    Users: Manage user accounts (create, update, delete).

    Reports: Create and manage report templates.

    Data Import: Bulk import data via CSV files.

API Endpoints

    Authentication:

        POST /api/auth/register: Register a new user.

        POST /api/auth/login: Authenticate and receive a JWT token.

    User Management:

        GET /api/users: List all users.

        POST /api/users: Create a new user.

        PUT /api/users/<id>: Update a user.

        DELETE /api/users/<id>: Delete a user.

    Reports:

        GET /api/reports: List all report templates.

        POST /api/reports: Create a new report template.

        PUT /api/reports/<id>: Update a report template.

        DELETE /api/reports/<id>: Delete a report template.

Contributing

    Fork the repository.

    Create a new branch:
    bash
    Copy

    git checkout -b feature/your-feature-name

    Commit your changes:
    bash
    Copy

    git commit -m "Add your feature"

    Push to the branch:
    bash
    Copy

    git push origin feature/your-feature-name

    Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For questions or feedback, please contact:

    Your Name

    Email: your.email@example.com

    GitHub: yourusername
