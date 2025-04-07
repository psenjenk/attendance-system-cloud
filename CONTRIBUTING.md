# Contributing to Cloud Attendance System

Thank you for your interest in contributing to the Cloud Attendance System! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature/fix
3. Make your changes
4. Test your changes
5. Submit a pull request

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/your-username/attendance-system-cloud.git
cd attendance-system-cloud
```

2. Set up the development environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pre-commit install
```

3. Create a `.env` file with development settings:
```bash
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
DB_NAME=attendance_db_dev
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

## Code Style

This project follows PEP 8 style guide and uses several tools to maintain code quality:

- Black for code formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking

Run the following commands to ensure your code meets our standards:

```bash
black .
isort .
flake8
mypy .
```

## Testing

Write tests for your changes and ensure all tests pass:

```bash
pytest
```

## Documentation

- Update documentation for any new features or changes
- Follow the existing documentation style
- Include docstrings for all new functions and classes

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the CHANGELOG.md with a summary of changes
3. Ensure all tests pass
4. Ensure code meets style requirements
5. Submit the pull request with a clear description of changes

## Commit Messages

Follow these guidelines for commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

Example:
```
Add user authentication system

- Implement JWT token authentication
- Add login/logout endpoints
- Update documentation

Fixes #123
```

## Questions?

If you have any questions, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue
4. Contact the maintainers 