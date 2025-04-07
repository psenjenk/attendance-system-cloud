# Cloud Attendance System

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-3.2%2B-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Issues](https://img.shields.io/github/issues/psenjenk/attendance-system-cloud.svg)](https://github.com/psenjenk/attendance-system-cloud/issues)
[![GitHub Stars](https://img.shields.io/github/stars/psenjenk/attendance-system-cloud.svg)](https://github.com/psenjenk/attendance-system-cloud/stargazers)

A Django-based cloud attendance system with REST API support, designed for educational institutions to manage student attendance efficiently.

![Cloud Attendance System](static/images/cloud.jpg)

## Features

- Student management
- Subject management
- Attendance tracking
- REST API support
- Role-based access control
- Secure authentication
- API documentation
- Logging and monitoring

### Student Management
![Student Management](static/images/student.PNG)

### Subject Management
![Subject Management](static/images/subjects.PNG)

### Attendance Tracking
![Attendance Tracking](static/images/attendance.PNG)

## Prerequisites

- Python 3.7+
- MySQL 5.7+
- pip
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/psenjenk/attendance-system-cloud.git
cd attendance-system-cloud
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```bash
# Django Settings
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com

# Database Settings
DB_NAME=attendance_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True
```

5. Set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Documentation

The API documentation is available at:
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

Example API endpoints:
```bash
# Authentication
POST /api/auth/login/ - User login
POST /api/auth/logout/ - User logout

# Students
GET /api/students/ - List all students
POST /api/students/ - Create new student
GET /api/students/{id}/ - Get student details

# Attendance
POST /api/attendance/ - Record attendance
GET /api/attendance/reports/ - Generate attendance reports
```

## Project Structure

```
attendance-system-cloud/
├── api_v1/                 # API application
│   ├── models.py          # Database models
│   ├── views.py           # API views
│   ├── serializers.py     # Data serializers
│   ├── schemas.py         # API documentation schemas
│   ├── permissions.py     # Custom permissions
│   └── utils.py           # Utility functions
├── Attendance_System/      # Django project
│   ├── settings.py        # Project settings
│   ├── urls.py           # URL configuration
│   └── wsgi.py           # WSGI configuration
├── templates/             # HTML templates
├── static/               # Static files
├── logs/                 # Log files
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Security Features

- Environment variable configuration
- Secure session handling
- CORS protection
- Password validation
- Token authentication
- Rate limiting
- XSS protection
- CSRF protection
- SQL injection prevention
- Secure password hashing
- HTTPS enforcement

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
This project follows PEP 8 style guide. To check code style:
```bash
flake8 .
```

### Pre-commit Hooks
Install pre-commit hooks:
```bash
pre-commit install
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please:
1. Check the [documentation](https://github.com/psenjenk/attendance-system-cloud/wiki)
2. Search [existing issues](https://github.com/psenjenk/attendance-system-cloud/issues)
3. Create a new issue if needed
4. Contact Kevin Psenjen for direct support
