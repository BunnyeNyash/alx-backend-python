# Messaging App API

## Overview

This project implements a robust RESTful API for managing messaging functionality using Django and Django REST Framework (DRF). The API includes endpoints for creating and listing conversations and messages, designed to follow modern architectural patterns and Django best practices. The application features a modular structure with data models for users, conversations, and messages, complete with serializers, viewsets, and URL routing.

## Features

- **User Management**: Extends Django’s `AbstractUser` for custom user profiles.
- **Conversation Management**: Tracks users involved in conversations with many-to-many relationships.
- **Message Handling**: Supports sending messages within conversations with nested relationships.
- **Secure Configuration**: Uses a `.env` file for sensitive data (e.g., `SECRET_KEY`) and `.gitignore` for security.
- **RESTful API**: Provides endpoints like `/api/conversations/` and `/api/messages/` via DRF’s browsable interface.
  
## Prerequisites

- **Ubuntu WSL** (or any Linux-based system)
- **Python 3.6+**
- **pip** (Python package manager)
- **Git** (optional, for version control)

## Installation

### 1. Clone the Repository

If using Git, clone the project:

```bash
git clone https://github.com/BunnyeNyash/alx-backend-python.git
cd alx-backend-python/messaging_app
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install django djangorestframework python-dotenv
```

### 4. Configure Environment Variables

1. Create a .env file in the project root (~/book_management):

```bash
vi .env
```

2. Add a secure SECRET_KEY (generate one with the command below) and other settings:

```
SECRET_KEY='your-secure-key-here'
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
```

- Generate a secure key:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

3. Save and exit the .env file using ESC then :wq

### 5. Apply Migrations

Set up the database:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 6. Run the Development Server

Start the server to test the API:

```bash
python3 manage.py runserver
```

- Visit http://127.0.0.1:8000/api/conversations/ in your browser to see the browsable API.

## Project Structure
```
messaging_app/
├── messaging_app/            # Project configuration
│   ├── __init__.py
│   ├── settings.py           # Configuration (e.g., SECRET_KEY, ALLOWED_HOSTS)
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI deployment
│   └── asgi.py               # ASGI deployment
├── chats/                    # App for messaging functionality
│   ├── migrations/           # Database migration files
│   ├── __init__.py
│   ├── models.py             # Defines User, Conversation, and Message models
│   ├── serializers.py        # Handles data serialization with relationships
│   ├── views.py              # Defines ConversationViewSet and MessageViewSet
│   └── urls.py               # URL configuration for the API
├── manage.py                 # Management command-line utility
├── .env                      # Environment variables (e.g., SECRET_KEY)
├── .gitignore                # Excludes sensitive files from Git
└── README.md                 # This file
```

## Configuration

- **.env**: Stores sensitive data like SECRET_KEY, DEBUG, and ALLOWED_HOSTS. Ensure .env is listed in .gitignore.
- **settings.py**: Loads .env variables and sets DEBUG and ALLOWED_HOSTS. Update ALLOWED_HOSTS for production domains.
- **.gitignore**: Prevents tracking of venv/, db.sqlite3, .env, and other local files (e.g., __pycache__/).

## Development Notes

- **Debug Mode**: Set DEBUG = True for development with detailed error pages, but use DEBUG = False with ALLOWED_HOSTS for production.
- **Testing**: Run migrations and test endpoints. Fix errors as they arise (e.g., missing imports, relationship issues).
- **Documentation**: This README serves as the primary documentation; consider adding inline comments in code.

## Tasks Completed
1. **Project Setup**: Initialized messaging_app with django-admin startproject, installed DRF, and created the chats app.
2. **Define Data Models**: Implemented User (extending AbstractUser), Conversation, and Message models in chats/models.py.
3. **Create Serializers**: Built serializers for User, Conversation, and Message in chats/serializers.py with nested relationships.
4. **Build API Endpoints**: Created ConversationViewSet and MessageViewSet in chats/views.py for CRUD operations.
5. **Set Up URL Routing**: Configured routes with DefaultRouter in chats/urls.py and included them in messaging_app/urls.py under /api/.
6. **Run and Fix Errors**: Executed migrations and tested the app with python3 manage.py runserver.

## Acknowledgments
- Built with Django and Django REST Framework.
- Part of the ALX "Building Robust APIs" project.
  
