# Django REST Framework (DRF)

Let's build a **Student Management REST API** from zero.

By the end, you will have an API that can:

* Create students
* Read students
* Read a single student
* Update students
* Delete students
* Store data in SQLite
* Return data as JSON
* Test APIs using the browser and `curl`

We will not skip the setup steps.

---

# 1. What We Are Going to Build

Our project will look like this:

```text
Student Management API

GET     /api/students/       → Get all students
POST    /api/students/       → Create student

GET     /api/students/1/     → Get student 1
PUT     /api/students/1/     → Update student 1
PATCH   /api/students/1/     → Partially update student 1
DELETE  /api/students/1/     → Delete student 1
```

Architecture:

```text
Client
  ↓
URL
  ↓
DRF ViewSet
  ↓
Serializer
  ↓
Django Model
  ↓
SQLite Database
```

---

# 2. Check Python Installation

Open Terminal / Command Prompt.

Run:

```bash
python --version
```

You should see something like:

```text
Python 3.x.x
```

If `python` doesn't work, try:

```bash
python3 --version
```

---

# 3. Create a Project Folder

Create a folder:

```bash
mkdir drf_student_api
```

Move inside it:

```bash
cd drf_student_api
```

---

# 4. Create a Virtual Environment

A virtual environment keeps project packages separate.

Run:

```bash
python -m venv venv
```

Your folder will now look approximately like:

```text
drf_student_api/
└── venv/
```

---

# 5. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, you should see something similar to:

```text
(venv)
```

at the beginning of your terminal line.

---

# 6. Install Django and DRF

Now install Django:

```bash
pip install django
```

Install Django REST Framework:

```bash
pip install djangorestframework
```

Or install both together:

```bash
pip install django djangorestframework
```

Check Django:

```bash
django-admin --version
```

---

# 7. Create Django Project

Run:

```bash
django-admin startproject student_api .
```

**Important:** The `.` at the end means create the project in the current folder.

Your structure should now look like:

```text
drf_student_api/
│
├── venv/
│
├── manage.py
│
└── student_api/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

# 8. Understand `manage.py`

`manage.py` is a command-line utility provided by Django.

We use it for things like:

```bash
python manage.py runserver
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py startapp
```

Think of `manage.py` as the **control panel of your Django project**.

---

# 9. Run Django for the First Time

Run:

```bash
python manage.py runserver
```

You should see something like:

```text
Starting development server at http://127.0.0.1:8000/
```

Open:

```text
http://127.0.0.1:8000/
```

If you see the Django welcome page, Django is working.

Stop the server:

```text
CTRL + C
```

---

# 10. Create a Django App

A Django project can contain multiple apps.

For our student API, create an app called `students`.

Run:

```bash
python manage.py startapp students
```

Now your structure becomes:

```text
drf_student_api/
│
├── venv/
│
├── manage.py
│
├── student_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── students/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

---

# 11. Add DRF and Students App

Open:

```text
student_api/settings.py
```

Find:

```python
INSTALLED_APPS = [
    ...
]
```

Add:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'students',
]
```

Now Django knows about:

1. Django REST Framework
2. Our `students` app

---

# 12. Create Student Model

Open:

```text
students/models.py
```

Replace its content with:

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
```

Let's understand it.

### `name`

```python
name = models.CharField(max_length=100)
```

Stores student name.

Example:

```text
Rahul
```

### `email`

```python
email = models.EmailField(unique=True)
```

Stores email.

`unique=True` means two students cannot have the same email.

### `course`

```python
course = models.CharField(max_length=100)
```

Stores course name.

Example:

```text
Python
```

### `age`

```python
age = models.IntegerField()
```

Stores integer values.

Example:

```text
22
```

---

# 13. Create Database Migration

Now Django needs to create database instructions based on our model.

Run:

```bash
python manage.py makemigrations
```

You should see something similar to:

```text
Migrations for 'students':
    students/migrations/0001_initial.py
```

---

# 14. Apply Migration

Now run:

```bash
python manage.py migrate
```

This creates the database tables.

Django uses SQLite by default.

You should now see a file:

```text
db.sqlite3
```

Your structure:

```text
drf_student_api/
│
├── db.sqlite3
├── manage.py
│
├── student_api/
│
├── students/
│
└── venv/
```

---

# 15. What is a Migration?

This is important for students.

We created:

```python
class Student(models.Model):
```

But the database doesn't automatically understand that.

Migration creates the required database changes.

Think:

```text
Python Model
     ↓
makemigrations
     ↓
Migration File
     ↓
migrate
     ↓
Database Table
```

---

# 16. Create a Serializer

Now comes one of the most important concepts in DRF.

Create a new file:

```text
students/serializers.py
```

Add:

```python
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
```

---

# 17. What is a Serializer?

A serializer converts Django model data into a format that can be sent through an API, usually JSON.

Think:

```text
Django Model
     ↓
Serializer
     ↓
JSON
```

For example, Django has:

```text
Student object
```

The serializer can convert it into:

```json
{
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "course": "Python",
    "age": 22
}
```

The serializer also performs the reverse process.

```text
JSON
 ↓
Serializer
 ↓
Django Model
 ↓
Database
```

This is why serializers are so important in DRF.

---

# 18. Create the API View

Open:

```text
students/views.py
```

Replace it with:

```python
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

This small amount of code gives us CRUD functionality.

`ModelViewSet` provides actions for:

```text
GET
POST
PUT
PATCH
DELETE
```

---

# 19. Understand `queryset`

This line:

```python
queryset = Student.objects.all()
```

means:

> Get all Student objects from the database.

For example, if the database contains:

```text
Rahul
Priya
Amit
```

then:

```python
Student.objects.all()
```

returns all three.

---

# 20. Understand `serializer_class`

This:

```python
serializer_class = StudentSerializer
```

tells DRF:

> Use `StudentSerializer` to convert and validate Student data.

So our ViewSet connects:

```text
Student Model
      ↓
StudentSerializer
      ↓
StudentViewSet
```

---

# 21. Create API URLs

Now we need to tell Django where our API lives.

Open:

```text
student_api/urls.py
```

Replace it with:

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet


router = DefaultRouter()

router.register(
    r'students',
    StudentViewSet,
    basename='student'
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

---

# 22. Understand the Router

This part:

```python
router = DefaultRouter()
```

creates a DRF router.

Then:

```python
router.register(
    r'students',
    StudentViewSet,
    basename='student'
)
```

connects our URL with the ViewSet.

Finally:

```python
path('api/', include(router.urls))
```

means our API URLs will start with:

```text
/api/
```

Therefore:

```text
/api/students/
```

becomes our student API.

---

# 23. Our Complete Project Structure

At this point, your project should look like:

```text
drf_student_api/
│
├── venv/
│
├── db.sqlite3
│
├── manage.py
│
├── student_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── students/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    └── views.py
```

---

# 24. Start the Server

Run:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/api/students/
```

You should see the **Django REST Framework Browsable API**.

Because we haven't added any students yet, there won't be any records.

---

# 25. Create Our First Student

We can use the DRF browser interface.

Open:

```text
http://127.0.0.1:8000/api/students/
```

Find the POST section.

Send:

```json
{
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "course": "Python",
    "age": 22
}
```

Click **POST**.

The response should look similar to:

```json
{
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "course": "Python",
    "age": 22
}
```

Congratulations.

You just created your first DRF API record.

---

# 26. Create More Students

Create another:

```json
{
    "name": "Priya",
    "email": "priya@gmail.com",
    "course": "Django",
    "age": 21
}
```

Another:

```json
{
    "name": "Amit",
    "email": "amit@gmail.com",
    "course": "Machine Learning",
    "age": 24
}
```

Now the database contains:

| ID | Name  | Email                                     | Course           | Age |
| -: | ----- | ----------------------------------------- | ---------------- | --: |
|  1 | Rahul | [rahul@gmail.com](mailto:rahul@gmail.com) | Python           |  22 |
|  2 | Priya | [priya@gmail.com](mailto:priya@gmail.com) | Django           |  21 |
|  3 | Amit  | [amit@gmail.com](mailto:amit@gmail.com)   | Machine Learning |  24 |

---

# 27. GET — Get All Students

Open:

```text
http://127.0.0.1:8000/api/students/
```

Make a GET request.

Response:

```json
[
    {
        "id": 1,
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "course": "Python",
        "age": 22
    },
    {
        "id": 2,
        "name": "Priya",
        "email": "priya@gmail.com",
        "course": "Django",
        "age": 21
    },
    {
        "id": 3,
        "name": "Amit",
        "email": "amit@gmail.com",
        "course": "Machine Learning",
        "age": 24
    }
]
```

This is:

```text
GET /api/students/
```

Meaning:

> Give me all students.

---

# 28. GET — Get One Student

Now open:

```text
http://127.0.0.1:8000/api/students/1/
```

Response:

```json
{
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "course": "Python",
    "age": 22
}
```

This means:

```text
GET /api/students/1/
```

> Give me student number 1.

---

# 29. POST — Create a Student

POST is used to create data.

Endpoint:

```text
/api/students/
```

JSON:

```json
{
    "name": "Neha",
    "email": "neha@gmail.com",
    "course": "Data Science",
    "age": 23
}
```

After POST:

```text
Database
    ↓
New Student Created
```

---

# 30. PUT — Update Complete Student

Suppose Rahul's information needs to be changed.

Endpoint:

```text
/api/students/1/
```

Method:

```text
PUT
```

Send:

```json
{
    "name": "Rahul Sharma",
    "email": "rahulsharma@gmail.com",
    "course": "Advanced Python",
    "age": 23
}
```

PUT generally represents a complete replacement/update of the resource.

---

# 31. PATCH — Update Part of Student

Suppose we only want to change the course.

Use:

```text
PATCH /api/students/1/
```

Send:

```json
{
    "course": "Django REST Framework"
}
```

The other fields remain unchanged.

So:

```text
PUT   → Complete update
PATCH → Partial update
```

---

# 32. DELETE — Delete Student

Suppose we want to delete student 3.

Send:

```text
DELETE /api/students/3/
```

Student 3 will be removed from the database.

---

# 33. CRUD in One Table

This is extremely important for beginners.

| HTTP Method | URL                | Purpose          |
| ----------- | ------------------ | ---------------- |
| GET         | `/api/students/`   | Get all students |
| POST        | `/api/students/`   | Create student   |
| GET         | `/api/students/1/` | Get one student  |
| PUT         | `/api/students/1/` | Update student   |
| PATCH       | `/api/students/1/` | Partially update |
| DELETE      | `/api/students/1/` | Delete student   |

Remember:

```text
CREATE → POST
READ   → GET
UPDATE → PUT / PATCH
DELETE → DELETE
```

This is **CRUD**.

---

# 34. Test API Using cURL

You don't have to use only the browser.

You can also use `curl`.

### GET

```bash
curl http://127.0.0.1:8000/api/students/
```

---

### POST

```bash
curl -X POST http://127.0.0.1:8000/api/students/ \
-H "Content-Type: application/json" \
-d "{\"name\":\"Ravi\",\"email\":\"ravi@gmail.com\",\"course\":\"Python\",\"age\":25}"
```

---

### GET One Student

```bash
curl http://127.0.0.1:8000/api/students/1/
```

---

### PUT

```bash
curl -X PUT http://127.0.0.1:8000/api/students/1/ \
-H "Content-Type: application/json" \
-d "{\"name\":\"Rahul Sharma\",\"email\":\"rahulsharma@gmail.com\",\"course\":\"Django\",\"age\":23}"
```

---

### PATCH

```bash
curl -X PATCH http://127.0.0.1:8000/api/students/1/ \
-H "Content-Type: application/json" \
-d "{\"course\":\"DRF\"}"
```

---

### DELETE

```bash
curl -X DELETE http://127.0.0.1:8000/api/students/1/
```

---

# 35. Understand the Complete Request

Let's understand what happens when we send:

```text
GET /api/students/
```

### Step 1 — Client

A browser, React application, mobile app, etc. sends:

```text
GET /api/students/
```

### Step 2 — URL

Django receives the URL.

The router finds:

```python
StudentViewSet
```

### Step 3 — ViewSet

The ViewSet executes the appropriate action.

For GET, it gets students from:

```python
Student.objects.all()
```

### Step 4 — Model

Django communicates with the database.

```text
Student Model
      ↓
SQLite
```

### Step 5 — Serializer

The serializer converts Django objects into JSON.

```text
Python/Django Object
        ↓
StudentSerializer
        ↓
JSON
```

### Step 6 — Response

The API returns:

```json
[
    {
        "id": 1,
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "course": "Python",
        "age": 22
    }
]
```

---

# 36. The Most Important DRF Diagram

Students should remember this:

```text
                    REQUEST
                       ↓
                /api/students/
                       ↓
                    URL Router
                       ↓
                 StudentViewSet
                       ↓
                  Serializer
                       ↓
                    Model
                       ↓
                   Database
                       ↓
                    Model
                       ↓
                  Serializer
                       ↓
                  JSON Response
                       ↓
                     CLIENT
```

---

# 37. Why Do We Need Serializer?

This is one of the most common beginner questions.

Suppose Django gives us a Python object:

```python
Student(
    id=1,
    name="Rahul",
    course="Python"
)
```

A frontend application doesn't want a Django Python object.

It wants something like:

```json
{
    "id": 1,
    "name": "Rahul",
    "course": "Python"
}
```

Serializer performs this conversion.

```text
Django Object
      ↓
   Serializer
      ↓
     JSON
```

And when the client sends JSON:

```text
JSON
 ↓
Serializer
 ↓
Django Object
 ↓
Database
```

So:

> **Serializer is the translator between Django data and API data.**

---

# 38. Why Do We Need ViewSet?

Our ViewSet is:

```python
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

`ModelViewSet` gives us common CRUD operations without writing every method ourselves.

Conceptually, it handles:

```text
list()
retrieve()
create()
update()
partial_update()
destroy()
```

So instead of writing separate code for:

```text
GET
POST
PUT
PATCH
DELETE
```

DRF gives us a lot of that functionality automatically.

---

# 39. Why Do We Need Router?

Normally, we would need to define many URLs manually.

For example:

```text
/api/students/
/api/students/1/
```

A DRF router automatically creates the URL patterns for our ViewSet.

We write:

```python
router = DefaultRouter()

router.register(
    r'students',
    StudentViewSet,
    basename='student'
)
```

And DRF generates the appropriate routes.

---

# 40. Add Admin Interface

We can also see students inside Django Admin.

Open:

```text
students/admin.py
```

Add:

```python
from django.contrib import admin
from .models import Student


admin.site.register(Student)
```

Now Django knows that `Student` should appear in the admin panel.

---

# 41. Create Admin User

Run:

```bash
python manage.py createsuperuser
```

Django will ask:

```text
Username:
Email:
Password:
Password (again):
```

Enter your details.

Then start the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

Login using your superuser.

You should see:

```text
Students
```

Click it to see your student records.

---

# 42. Important Files and Their Jobs

Now let's understand every important file.

### `models.py`

Defines database structure.

```python
class Student(models.Model):
```

Think:

> What data should we store?

---

### `serializers.py`

Converts and validates API data.

```python
class StudentSerializer(serializers.ModelSerializer):
```

Think:

> How should data move between Django and JSON?

---

### `views.py`

Contains API logic.

```python
class StudentViewSet(viewsets.ModelViewSet):
```

Think:

> What should happen when the API is called?

---

### `urls.py`

Defines API routes.

```python
router.register(...)
```

Think:

> Which URL should call which API?

---

### `settings.py`

Contains project configuration.

Think:

> How is the Django project configured?

---

### `models.py → serializers.py → views.py → urls.py`

A simple way to remember the relationship:

```text
Model
 ↓
Serializer
 ↓
ViewSet
 ↓
URL
```

---

# 43. Complete Code — `models.py`

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
```

---

# 44. Complete Code — `serializers.py`

```python
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
```

---

# 45. Complete Code — `views.py`

```python
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

# 46. Complete Code — `urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet


router = DefaultRouter()

router.register(
    r'students',
    StudentViewSet,
    basename='student'
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

---

# 47. Complete Code — `settings.py`

The important section is:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'students',
]
```

---

# 48. Complete Code — `admin.py`

```python
from django.contrib import admin
from .models import Student


admin.site.register(Student)
```

---

# 49. Commands You Need to Remember

### Create project

```bash
django-admin startproject student_api .
```

### Create app

```bash
python manage.py startapp students
```

### Install DRF

```bash
pip install djangorestframework
```

### Create migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

### Create admin user

```bash
python manage.py createsuperuser
```

### Start server

```bash
python manage.py runserver
```

---

# 50. Final API Testing

After running:

```bash
python manage.py runserver
```

Test these URLs:

### All Students

```text
http://127.0.0.1:8000/api/students/
```

### Student 1

```text
http://127.0.0.1:8000/api/students/1/
```

### Admin

```text
http://127.0.0.1:8000/admin/
```

---

# 51. What You Have Learned

After completing this project, you understand the basic DRF workflow:

```text
1. Install Django
        ↓
2. Install DRF
        ↓
3. Create Django Project
        ↓
4. Create Django App
        ↓
5. Add DRF to settings.py
        ↓
6. Create Model
        ↓
7. Create Migration
        ↓
8. Apply Migration
        ↓
9. Create Serializer
        ↓
10. Create ViewSet
        ↓
11. Create Router
        ↓
12. Create API URLs
        ↓
13. Run Server
        ↓
14. Test API
```

And the core architecture is:

```text
              CLIENT
                 ↓
              HTTP
                 ↓
               URL
                 ↓
             VIEWSET
                 ↓
            SERIALIZER
                 ↓
               MODEL
                 ↓
             DATABASE
                 ↓
               MODEL
                 ↓
            SERIALIZER
                 ↓
              JSON
                 ↓
              CLIENT
```

## The 5 things to remember

If you're a beginner, focus on these five first:

**1. Model** → Database structure

**2. Serializer** → Django data ↔ JSON

**3. View/ViewSet** → API logic

**4. URL/Router** → API endpoint

**5. HTTP Methods** → CRUD operations

```text
GET     → Read
POST    → Create
PUT     → Update
PATCH   → Partial Update
DELETE  → Delete
```

Once these concepts are clear, the next natural step is to build the same project with **authentication, permissions, validation, search, filtering, pagination, and JWT login**, which is where DRF starts becoming useful for real-world applications.
