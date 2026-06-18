# Enterprise Task & Note Manager API

A production-ready, multi-tenant RESTful API built with Django REST Framework. This project demonstrates enterprise-level backend architecture, focusing on relational data integrity, secure stateless authentication, and strict object-level permissions.

## Tech Stack
* **Framework:** Django & Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Containerization:** Docker & Docker Compose
* **Authentication:** JSON Web Tokens (JWT) via `djangorestframework-simplejwt`
* **Adapter:** `psycopg2-binary`

## Enterprise Features Implemented
1. **Custom User Model:** Replaced Django's default user model with a custom, email-based authentication system before initial migrations to ensure future scalability.
2. **Relational Database Integrity:** Implemented 1-to-Many relationships (`User` -> `Tasks` -> `Notes`) utilizing Foreign Keys with `CASCADE` delete rules to prevent orphan records.
3. **Nested Serializers:** Engineered complex JSON payloads where a single `Task` request dynamically fetches and nests all associated `Notes` using reverse relationships (`related_name`).
4. **Data Isolation & Object-Level Permissions:** * Overrode QuerySets to ensure users can only ever retrieve their own data.
    * Built custom permission classes (`IsOwner`) to verify database row ownership before allowing `UPDATE` or `DELETE` operations.
5. **Stateless Security:** Secured all endpoints using dual-token JWT architecture (short-lived Access tokens, long-lived Refresh tokens).
6. **Containerized Infrastructure:** Abstracted the PostgreSQL database into an isolated Docker container with local volume mapping.

## Project Structure
```text
enterprise_task_manager/
│
├── core/                 # Main configuration, settings, and global URLs
├── accounts/             # App: Handles Custom User Model & Auth Logic
├── tasks/                # App: Handles Task & Note models, views, and permissions
├── docker-compose.yml    # PostgreSQL container configuration (Port 5466)
├── requirements.txt      # Python dependencies
└── manage.py             # Django entry point


## API Endpoints
**Authentication** (accounts & core)

* 'POST /api/auth/login/' - Accepts username/password, returns JWT access and refresh tokens.

* 'POST /api/auth/refresh/' - Accepts a refresh token to generate a new access token.

**Tasks & Notes** (tasks) - Requires JWT Access Token

* 'GET /api/tasks/' - Lists all tasks belonging to the authenticated user (Notes nested inside).

* 'POST /api/tasks/' - Creates a new task and automatically assigns it to the authenticated user.

* 'GET /api/tasks/<id>/' - Retrieves details of a specific task (must be the owner).

* 'PUT /api/tasks/<id>/' - Updates a specific task (must be the owner).

* 'DELETE /api/tasks/<id>/'- Deletes a specific task and cascades deletion to all attached notes (must be the owner).

### Local Setup Instructions
1. **Clone the repository**
git clone <your-repo-url>
cd enterprise_task_manager

2. **Spin up the PostgreSQL Database via Docker**
docker-compose up -d
(Note: Ensure Docker Desktop is running. The database runs on port 5466 to avoid conflicts).

3.**Set up the Python Virtual Environment**

### Bash
python -m venv venv

## Activate on Windows:
venv\Scripts\activate  
## Activate on Mac/Linux:
## source venv/bin/activate 

4. **Install Dependencies**
pip install -r requirements.txt

5. **Apply Database Migrations**
python manage.py makemigrations accounts
python manage.py makemigrations tasks
python manage.py migrate

6. **Create a Superuser & Run the Server **
python manage.py createsuperuser
python manage.py runserver