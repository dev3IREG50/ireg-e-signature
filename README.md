# Backend API Documentation

Welcome to the Backend API documentation for the e-signature.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [1. Remove Team Members](#1-remove-team-members)
- [License](#license)

## Introduction

This project is inspired by the functionalities provided by signrequest.com, offering users a comprehensive platform for managing sign requests and documents. The system encompasses a range of features designed to enhance document handling, team collaboration, and security measures.

## Key Features

1. **Email-Based Signing Requests:**

   - Streamlined signing requests through a user-friendly email system.

2. **Document Management:**

   - Efficient tools for organizing, tracking, and accessing documents.

3. **Document Log Generation:**

   - Robust logging system capturing detailed records of document-related activities.

4. **Security Measures:**

   - Implementation of robust security protocols to safeguard sensitive data.

5. **Permission System:**

   - Versatile access control, ensuring data privacy and security.

6. **Team Collaboration:**

   - Features facilitating seamless collaboration among team members.

7. **User Management within Teams:**

   - Tools for efficient user management within teams.

8. **Different User Roles:**

   - Support for diverse user roles, tailoring access levels based on responsibilities.

9. **User Invitation via Email:**

   - Simplified onboarding through email invitations.

10. **RESTful APIs:**

    - Over 20 RESTful APIs provided for seamless integration with the frontend.

11. **User Authentication with Simple JWT:**
    - Secure user authentication powered by Simple JWT (JSON Web Tokens).

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST framework
- asgiref==3.7.2
- black==23.12.1
- chardet==5.2.0
- click==8.1.7
- colorama==0.4.6
- Django==5.0.1
- django-cors-headers==4.3.1
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.3.1
- mypy-extensions==1.0.0
- packaging==23.2
- pathspec==0.12.1
- pillow==10.2.0
- platformdirs==4.1.0
- PyJWT==2.8.0
- pytz==2023.3.post1
- reportlab==4.0.9
- sqlparse==0.4.4
- tzdata==2023.4

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dev3IREG50/ireg-e-signature.git
   ```
2. Navigate to the project directory:
   ```bash
   cd signrequest_backend
   ```
3. Create a virtual environment:
   - First install the virtual environemt
   ```bash
   python -m pip install virtualenv
   ```
   - Activate the virtual environment
   ```bash
   python -m env\scripts\activate (if you use VS code, it will automatically opens the virtual environment)
   ```
4. Install dependacies:
   ```bash
   pip install -r requirements.txt
   ```
5. If you use your own database server don't forget to make migrations
6. Start the server:
   ```bash
   python manage.py runserver
   ```

### Navigating the Project:

Once you've successfully set up the project, head over to the base/api folder—it's
the heart of the implementation. Here's a breakdown of what you'll find in key directories:

###### custom_views:

- In this directory, you'll discover all the endpoints meticulously organized with modular and class documentation.
- Each endpoint is detailed and designed to be easily understood, ensuring a smooth exploration of the codebase.

###### utils:

- Dive into the utils folder to explore a collection of utility functions. Notably, this includes the logic behind email functionalities.

###### permissions:

- The permissions folder houses all the logic related to permissions, providing a centralized location for managing access controls.

###### Code Organization:

- My commitment to clarity is evident in the meticulous organization of the codebase.
  Detailed documentation accompanies each module and class, facilitating an intuitive understanding of the code.

Feel free to explore the project, and you'll find that the code is not just functional but also organized and easy to follow. If you have any questions or need further assistance, don't hesitate to reach out. Happy coding!
