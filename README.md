# Cloud Attendance System

A Django-based cloud attendance system with REST API support.

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
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
DB_NAME=attendance_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
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

The API documentation is available at `/swagger/` and `/redoc/` when running the development server.

## Project Structure

```
attendance-system-cloud/
├── api_v1/                 # API application
│   ├── models.py          # Database models
│   ├── views.py           # API views
│   ├── serializers.py     # Data serializers
│   └── schemas.py         # API documentation schemas
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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact Kevin Psenjen.
