# Grading System Project

## Description

This project is a grading management system for educational institutions. Teachers can enter grades for students, the secretariat can confirm these grades, and students can view their detailed grades.

## Technologies

- **Django**: Web framework used for developing the application.
- **PostgreSQL**: Database used for storing data.
- **Docker**: Used for isolating the development and production environments.
- **Docker Compose**: Used for easier management of Docker services.

## Requirements

Before starting, ensure that you have the following installed:

- Docker
- Docker Compose
- Python 3.x
- pip

## Installation

1. **Clone το repository:**
   ```bash
   git clone https://github.com/nikos-kaparos/grade_managemnet/tree/main
   cd grading_system
2. **Set up the Docker environment:**
    ```bash
   docker-compose up --build
3. **Run the database migrations:**
   ```bash
   docker-compose run web python manage.py makemigrations
   docker-compose run web python manage.py migrate
4. **Create a superuser (optional):**
   ```bash
   docker-compose run web python manage.py createsuperuser
## Access the application:
Open your browser and go to http://localhost:8000
## Usage
   Login:
      To log in, you must have an account. Students' usernames must begin with "it".
      The user groups include:
         Teacher
         Secretariat
         Students
   Features:
      Teachers can add grades.
      The secretariat can confirm grades.
      Students can view their detailed grades.
