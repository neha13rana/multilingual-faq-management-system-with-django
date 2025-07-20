# Multilingual FAQ Management System with Django

## Overview
This project provides a robust solution for managing FAQs in multiple languages. It includes advanced features such as WYSIWYG editor support, API endpoints for multilingual operations, caching for improved performance, and a well-documented workflow for deployment and testing.

---

## Table of Contents
1. [Installation](#installation)
2. [Features](#features)
3. [API Usage](#api-usage)
4. [Unit Testing](#unit-testing)
5. [Caching with Redis](#caching-with-redis)
6. [Screenshots](#screenshots)
7. [Contributing](#contributing)

---

## Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/neha13rana/multilingual-faq-management-system-with-django.git
   cd multilingual-faq-management-system-with-django
   ```

2. Activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

3. Run the server:
   ```bash
   python manage.py runserver
   ```

---

## Features

- **Multilingual FAQ Management**: Add, update, and retrieve FAQs in multiple languages.
- **WYSIWYG Editor Integration**: Format FAQ answers with the django-ckeditor.
- **Dynamic API**: Language support using query parameters (`?lang=en`, `?lang=hi`, etc.).
- **Caching**: Redis-based caching for faster performance.
- **Admin Dashboard**: User-friendly admin panel for managing FAQs.
- **Testing**: Comprehensive unit tests for models and APIs.

---

## API Usage

### Admin Panel
- Access the admin panel:
  ```
  http://localhost:8000/admin/
  ```
  Use this panel to manage FAQs with a rich-text editor.

### FAQ List
- Retrieve FAQs:
  ```
  http://localhost:8000/faq_app/faq-list/
  ```
- Retrieve FAQs in a specific language:
  ```
  http://localhost:8000/faq_app/faq-list/?lang=hi
  ```

### Submit FAQ
- Add a new FAQ:
  ```
  http://localhost:8000/faq_app/submit/
  ```

---

## Unit Testing

- **Framework**: `pytest`
- **Test Cases**:
  - API testing:
    - `faqlist` with language parameter
    - `submit_faq`
    - `faq_list`
  - Model testing:
    - FAQ creation
    - FAQ translation

Run the tests:
```bash
pytest
```

---

## Caching with Redis

Enable caching for performance enhancements:

1. Start a Redis container using Docker:
   ```bash
   docker run --name redis-container -p 6379:6379 -d redis
   ```
2. Verify the container is running:
   ```bash
   docker ps
   ```

---

## Screenshots

### Admin Panel
![Admin Panel](https://github.com/user-attachments/assets/9947f9bc-9d65-484a-8053-a62a00883726)

### FAQ Management
![FAQ Management](https://github.com/user-attachments/assets/b4d83a6d-0aab-4867-bd38-5b731d7ff693)

### WYSIWYG Editor
![WYSIWYG Editor](https://github.com/user-attachments/assets/efa3c23a-bf16-4434-bb73-f22c63ed27cf)

### Multilingual Support
![Multilingual Support](https://github.com/user-attachments/assets/4e742c05-9fe7-4eb6-8ec5-dbe8f4e91298)

---


