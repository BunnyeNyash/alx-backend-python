# Event Listeners (Signals), ORM & Advanced ORM Techniques

## Django Signals, ORM, and Caching Project

This project implements a messaging application using Django, focusing on advanced features like Signals, Advanced ORM Techniques, and Caching. It is part of the `alx-backend-python` repository under the `Django-signals_orm-0x04` directory.

### Repository

- GitHub: [alx-backend-python](https://github.com/BunnyeNyash/alx-backend-python.git)
- Directory: `Django-signals_orm-0x04`

### Project Structure
```
Django-signals_orm-0x04/
    ├── messaging_app/                # Django project directory
    │   ├── messaging_app/
    │   │   ├── __init__.py
    │   │   ├── settings.py          # Project settings (for caching)
    │   │   ├── urls.py              # Project URL configuration
    │   │   └── wsgi.py
    │   └── manage.py
    ├── messaging/                    # Django app directory
    │   ├── __init__.py
    │   ├── admin.py                 # Admin panel configuration
    │   ├── apps.py                  # App configuration
    │   ├── models.py                # Database models
    │   ├── signals.py               # Signal handlers
    │   ├── tests.py                 # Test cases
    │   ├── urls.py                  # App URL configuration
    │   ├── views.py                 # View logic
    │   ├── templates/
    │   │   └── messaging/
    │   │       ├── conversation.html
    │   │       ├── inbox.html
    │   │       └── threaded.html
    │   └── migrations/
    │       ├── __init__.py
    └── README.md
```

### How to Use
1. Clone the Repository and then navigate to `Django-signals_orm-0x04/messaging_app`

```bash
git clone https://github.com/BunnyeNyash/alx-backend-python.git
cd Django-signals_orm-0x04/messaging_app
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install and save dependencies:

```bash
pip install django
pip freeze > requirements.txt
```

4. Run Migrations

```bash
python manage.py makemigrations && python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

## Tasks
- Task 0: Implement Signals for User Notifications
  - **Objective:** Automatically notify users when they receive a new message.
    
- Task 1: Create a Signal for Logging Message Edits
  - **Objective:** Log when a user edits a message and save the old content before the edit.
    
- Task 2: Use Signals for Deleting User-Related Data
  - **Objective:** Automatically clean up related data when a user deletes their account.
    
- Task 3: Leverage Advanced ORM Techniques for Threaded Conversations
  - **Objective:** Implement threaded conversations where users can reply to specific messages, and retrieve conversations efficiently.
    
- Task 4: Custom ORM Manager for Unread Messages
  - **Objective:** Create a custom manager to filter unread messages for a user.
    
- Task 5: Implement Basic view cache
  - **Objective:** Set up basic caching for a view that retrieves messages in the messaging app.

