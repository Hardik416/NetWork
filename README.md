# NetWork

NetWork is a Django-based professional networking platform with profile management, authentication, job browsing, and REST API support.

## Features

- User authentication (signup, login, logout)
- Professional profile creation and editing
- Experience, education, and skill management
- Profile image upload support
- Job listing, job detail, and job posting pages
- Basic job application endpoint
- REST API endpoints for profiles, experiences, educations, and skills

## Tech Stack

- Python 3
- Django 5
- Django REST Framework
- SQLite (default)
- HTML/CSS templates + static assets

## Project Structure

- `NetWorkDjango/` – Django project configuration (`settings.py`, `urls.py`)
- `network_auth/` – authentication and profile-related models
- `network_core/` – profile creation/editing and profile views
- `network_jobs/` – job listing/searching/posting views
- `network_api/` – REST API viewsets and serializers
- `templates/` – HTML templates
- `static/` – static files

## Setup & Run

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install djangorestframework
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Start development server:
   ```bash
   python manage.py runserver
   ```
6. Open in browser:
   - App: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Main Routes

- `/` – Login/Register page
- `/profile/` – User profile
- `/profile/create/` – Create/Edit profile
- `/jobs/` – Job listings
- `/jobs/search/` – Job search UI
- `/jobs/post/` – Post a job (login required)
- `/api/` – API root

## API Endpoints

Under `/api/` (router-based):

- `profiles/`
- `experiences/`
- `educations/`
- `skills/`

Authentication for API uses Django session auth (`/api/api-auth/`).

## Notes

- Default database is SQLite (`db.sqlite3`).
- Media uploads are served in development when `DEBUG=True`.
- Some job data in `network_jobs/views.py` is currently sample/static data.
