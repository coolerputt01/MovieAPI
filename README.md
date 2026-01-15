# Movie API 🎬

## Overview
A high-performance RESTful API built with Python and the Django REST Framework designed to synchronize, store, and manage Star Wars film data. The system integrates with external APIs (SWAPI) to populate a local PostgreSQL database and provides a robust commenting engine with support for pagination and analytical aggregates.

## Features
- Django REST Framework: Implements a scalable architecture for API development and serialization.
- External API Synchronization: Custom utility to fetch and update film data from the Star Wars API (SWAPI).
- PostgreSQL Integration: Relational data storage ensuring data integrity for films and user-generated comments.
- Dynamic Aggregates: Automated comment counting and chronological sorting for film listings.
- API Documentation: Automated OpenAPI 3.0 schema generation using drf-spectacular.
- Pagination: Optimized list views for handling large volumes of comment data.

## Getting Started
### Installation
1. Clone the repository to your local machine.
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required dependencies:
   pip install django djangorestframework psycopg2-binary requests python-dotenv drf-spectacular
4. Apply database migrations:
   python manage.py migrate
5. Start the development server:
   python manage.py runserver

### Environment Variables
Create a .env file in the root directory and configure the following variables:
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

## API Documentation
### Base URL
/api/

### Endpoints

#### POST /api/sync-films/
**Request**:
No payload required.

**Response**:
{
  "msg": "Database successfully synced!"
}

**Errors**:
- 500: External service connection failure.

#### GET /api/films/
**Request**:
No payload required. Returns a list of all films in the database.

**Response**:
[
  {
    "id": 1,
    "swapiFilm_id": 1,
    "film_title": "A New Hope",
    "release_date": "1977-05-25",
    "comment_count": 5
  }
]

**Errors**:
- 200: Returns empty list if no films exist.

#### POST /api/film/<int:film_id>/comments/create/
**Request**:
{
  "content": "This is a technical comment about the cinematography."
}

**Response**:
{
  "id": 12,
  "film_id": 1,
  "content": "This is a technical comment about the cinematography.",
  "created_at": "2023-10-27T14:30:00Z"
}

**Errors**:
- 404: Film not found.
- 400: Content field is missing or empty.

#### GET /api/film/<int:film_id>/comments/
**Request**:
No payload required. Returns all comments for a specific film ordered by creation date.

**Response**:
[
  {
    "id": 1,
    "film_id": 1,
    "content": "Excellent story.",
    "created_at": "2023-10-27T10:00:00Z"
  }
]

**Errors**:
- 404: Film not found.

#### GET /api/film/<int:film_id>/comments/paged/
**Request**:
Query Parameters:
- page: (optional) Page number.
- page_size: (optional) Number of items per page.

**Response**:
{
  "count": 50,
  "next": "http://api.url/api/film/1/comments/paged/?page=2",
  "previous": null,
  "results": [
    {
      "id": 50,
      "film_id": 1,
      "content": "Latest comment.",
      "created_at": "2023-10-27T16:00:00Z"
    }
  ]
}

**Errors**:
- 404: Film not found.

## Technologies Used
| Technology | Purpose | Link |
| --- | --- | --- |
| Python | Primary Programming Language | [Visit](https://www.python.org/) |
| Django | Web Framework | [Visit](https://www.djangoproject.com/) |
| Django REST Framework | API Toolkit | [Visit](https://www.django-rest-framework.org/) |
| PostgreSQL | Relational Database | [Visit](https://www.postgresql.org/) |
| drf-spectacular | Documentation Engine | [Visit](https://github.com/tfranzel/drf-spectacular) |

## Usage
The system is designed to be self-populating. Upon first deployment, users should call the `sync-films/` endpoint to hydrate the database with data from the SWAPI source. Once synchronized, the API allows for public listing of films and a community-driven comment system where users can discuss specific entries. 

Detailed documentation and interactive testing can be accessed via the Swagger UI at `/api/docs/` or Redoc at `/api/redoc/` when the server is running.

## Contributing
- 📥 Fork the repository and create your feature branch.
- 🛠 Ensure all code adheres to PEP 8 standards.
- 🧪 Write unit tests for any new features or bug fixes.
- 📝 Update the documentation if you are changing API behavior.
- 🚀 Submit a pull request with a clear description of your changes.

## Author Info
**[Your Name]**
- Website: [Your Website Link]
- LinkedIn: [Your LinkedIn Profile]
- Twitter: [Your Twitter Handle]

---
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

[![Readme was generated by Dokugen](https://img.shields.io/badge/Readme%20was%20generated%20by-Dokugen-brightgreen)](https://www.npmjs.com/package/dokugen)