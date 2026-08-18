## What is Django REST Framework (DRF)?

**Django REST Framework (DRF)** is a powerful toolkit built on top of **Django** that helps us create **Web APIs** easily.

In simple words:

> **Django is used to build web applications, while DRF helps Django communicate with other applications through APIs.**

### First, understand the problem

Imagine you have a **Student Management System** built with Django.

Your database contains:

| ID | Name  | Course           |
| -: | ----- | ---------------- |
|  1 | Rahul | Python           |
|  2 | Priya | Django           |
|  3 | Amit  | Machine Learning |

Now suppose a **mobile app** wants to get this student data.

The mobile app cannot directly access your Django database.

Instead:

**Mobile App → API → Django → Database**

The API acts as a **bridge** between the application and the backend.

---

## What exactly is an API?

API stands for:

**Application Programming Interface**

Think of an API like a **waiter in a restaurant**.

You are the customer → Mobile/Web App
Kitchen → Database/Backend
Waiter → API

You tell the waiter:

> "Give me the student with ID 1."

The API sends the request to Django.

Django gets the data from the database and sends it back through the API.

```text
Client
  ↓
API Request
  ↓
Django + DRF
  ↓
Database
  ↓
Django + DRF
  ↓
API Response
  ↓
Client
```

---

# Why do we need DRF?

Django itself can create APIs, but doing everything manually can become difficult.

DRF provides ready-made tools for:

* Creating APIs
* Handling HTTP requests
* Converting Django data into JSON
* Validating data
* Authentication
* Permissions
* Serialization
* CRUD operations
* API testing
* Browsable API interface

So instead of writing lots of code manually, DRF makes API development much easier.

---

# Django vs DRF

A simple way to remember it:

| Django                     | Django REST Framework              |
| -------------------------- | ---------------------------------- |
| Builds web applications    | Builds Web APIs                    |
| Returns HTML pages         | Usually returns JSON               |
| Uses templates             | Uses serializers                   |
| Browser-based applications | Mobile/Web/External applications   |
| Backend framework          | API development toolkit for Django |

For example, normal Django might return:

```html
<h1>Hello Rahul</h1>
```

DRF can return:

```json
{
    "id": 1,
    "name": "Rahul",
    "course": "Python"
}
```

This JSON can easily be consumed by:

* React
* Angular
* Vue
* Android
* iOS
* Flutter
* Another Python application
* Another backend service

---

# What is JSON?

JSON stands for **JavaScript Object Notation**.

It is a common format for exchanging data between applications.

Example:

```json
{
    "id": 1,
    "name": "Rahul",
    "course": "Python"
}
```

Think of JSON as a **common language between frontend and backend**.

---

# Important DRF Concepts

There are a few important concepts students should understand.

### 1. Model

The **Model** represents database data.

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
```

---

### 2. Serializer

A **Serializer** converts Django/Python objects into JSON and can also convert incoming JSON into Python/Django data.

Think:

```text
Django Object
     ↓
Serializer
     ↓
JSON
```

Example:

```json
{
    "id": 1,
    "name": "Rahul",
    "course": "Python"
}
```

This is one of the **most important concepts in DRF**.

---

### 3. View

The **View** handles the API request.

For example:

```text
GET /students/
```

The view decides:

> "What should I return when someone requests `/students/`?"

---

### 4. URL

The URL tells Django which API should be called.

Example:

```text
/api/students/
```

---

### 5. HTTP Methods

DRF commonly works with HTTP methods:

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Read data             |
| POST   | Create data           |
| PUT    | Update data           |
| PATCH  | Partially update data |
| DELETE | Delete data           |

You can remember:

```text
GET     → Read
POST    → Create
PUT     → Update
PATCH   → Partial Update
DELETE  → Delete
```

---

# Example: Student API

Suppose we create:

```text
/api/students/
```

### GET

Request:

```http
GET /api/students/
```

Response:

```json
[
    {
        "id": 1,
        "name": "Rahul",
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "course": "Django"
    }
]
```

We are **reading students**.

---

### POST

Request:

```http
POST /api/students/
```

Data:

```json
{
    "name": "Amit",
    "course": "Machine Learning"
}
```

Now a new student can be created.

---

### DELETE

```http
DELETE /api/students/1/
```

This can delete student ID `1`.

---

# The complete DRF flow

This is the most important diagram for beginners:

```text
             CLIENT
       React / Mobile App
                |
                | HTTP Request
                ↓
             URL
      /api/students/
                |
                ↓
              VIEW
                |
                ↓
            SERIALIZER
                |
                ↓
             MODEL
                |
                ↓
            DATABASE
                |
                ↓
             MODEL
                |
                ↓
            SERIALIZER
                |
                ↓
          JSON RESPONSE
                |
                ↓
             CLIENT
```

### In very simple words:

**Client asks → DRF processes → Database provides data → DRF converts it to JSON → Client receives it.**

---

# How to install DRF

First install Django:

```bash
pip install django
```

Then install Django REST Framework:

```bash
pip install djangorestframework
```

Add it to `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Now your Django project can use DRF.

---

# Real-world example

Imagine you have an **e-commerce application**.

The frontend wants product information.

It sends:

```http
GET /api/products/
```

DRF communicates with Django.

Django gets products from the database.

DRF converts them into JSON:

```json
[
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 800
    }
]
```

The frontend receives this JSON and displays the products.

So:

```text
React / Android
       ↓
      API
       ↓
     DRF
       ↓
    Django
       ↓
   Database
```

## One-line definition for students

> **Django REST Framework is a toolkit built on Django that makes it easy to create Web APIs for sending and receiving data, usually in JSON format.**

### Easy memory trick

**Django = Web Application**

**DRF = API for Django**

And remember the basic DRF building blocks:

**Model → Serializer → View → URL → API Response**.
