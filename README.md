### Enterprise Task & Note Manager API

A production-ready, multi-tenant RESTful API built with Django REST Framework. This project demonstrates enterprise-level backend architecture, focusing on relational data integrity, secure stateless authentication, strict object-level permissions, and a decoupled Client-Server architecture.

## Enterprise Features Implemented

Custom User Model: Replaced Django's default user model with a custom, email-based authentication system before initial migrations to ensure future scalability.

Relational Database Integrity: Implemented 1-to-Many relationships (User -> Tasks -> Notes) utilizing Foreign Keys with CASCADE delete rules to prevent orphan records.

Nested Serializers: Engineered complex JSON payloads where a single Task request dynamically fetches and nests all associated Notes using reverse relationships (related_name).

Data Isolation & Object-Level Permissions: * Overrode QuerySets to ensure users can only ever retrieve their own data.

Built custom permission classes (IsOwner) to verify database row ownership before allowing UPDATE or DELETE operations.

Decoupled Frontend Architecture: Built a standalone Vanilla JS and Bootstrap 5 frontend dashboard to consume the API, proving cross-origin resource sharing (CORS) and token injection capabilities.

Automated CI/CD & Cloud Hosting: Abstracted deployment using GitHub Actions for automated testing and continuous delivery to Render, backed by a live serverless PostgreSQL database (Neon).

## Tech Stack

Backend: Python 3, Django, Django REST Framework (DRF)

Database: PostgreSQL (Cloud-hosted via Neon, psycopg2-binary)

Frontend (Client): HTML5, Bootstrap 5, Vanilla JavaScript (Fetch API)

Deployment & CI/CD: Render, GitHub Actions

Security: JSON Web Tokens (JWT) via djangorestframework-simplejwt

## Project Structure

enterprise_task_manager/
│
├── core/                 # Main configuration, settings, and global URLs
├── accounts/             # App: Handles Custom User Model & Auth Logic
├── tasks/                # App: Handles Task & Note models, views, and permissions
├── frontend/             # Client: Standalone HTML/JS Dashboard
├── requirements.txt      # Python dependencies
└── manage.py             # Django entry point


## API Endpoints

Authentication (accounts & core)

POST /api/auth/login/ - Accepts username/password, returns JWT Access and Refresh tokens.

POST /api/auth/refresh/ - Accepts a refresh token to generate a new access token.

Tasks (tasks) - Requires JWT Access Token

GET /api/tasks/ - Lists all tasks for the logged-in user (supports ?search= and ?page=).

POST /api/tasks/ - Creates a new task and assigns it to the authenticated user.

GET /api/tasks/<id>/ - Retrieves details of a specific task (must be the owner).

PUT /api/tasks/<id>/ - Updates a specific task (must be the owner).

DELETE /api/tasks/<id>/- Deletes a specific task and cascades deletion to all attached notes.

Notes (tasks) - Requires JWT Access Token

POST /api/tasks/<id>/notes/ - Creates a new note attached to a specific task.

## Local Setup Instructions

# Clone the repository

git clone [https://github.com/bikrant0/enterprise-task-api-django.git](https://github.com/bikrant0/enterprise-task-api-django.git)
cd enterprise-task-api-django


Set up the Python Virtual Environment

# Windows
python -m venv venv
venv\Scripts\activate 

# Mac/Linux
python3 -m venv venv
source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


Apply Database Migrations

python manage.py makemigrations accounts
python manage.py makemigrations tasks
python manage.py migrate


Create a Superuser & Run the Server

python manage.py createsuperuser
python manage.py runserver


Run the Frontend Dashboard
Open frontend/index.html directly in your web browser (Chrome/Edge/Firefox) to interact with the API visually.
