# Django 

# Django Cheatsheet

## Introduction
[Django](https://www.djangoproject.com/) is a Python-based web framework designed for rapid development of web applications.

### Installation
Install Django using pip:

```bash
pip install django
```

### Creating a Project
Create a new project:

```bash
django-admin startproject projectName
```

### Starting a Server
Start the development server:

```bash
python manage.py runserver
```

## Django MVT Architecture
Django follows the Model-View-Template (MVT) architecture.

### Sample Model
Define a model representing the database schema:

```python
from django.db import models

class Product(models.Model):
    product_id = models.AutoField
```

### Sample views.py
Views decide what data gets delivered to the template:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Django CodesWithpankaj Cheatsheet")
```

### Sample HTML Template
A sample HTML file containing HTML, CSS, and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>CodesWithpankaj Cheatsheet</title>
</head>
<body>
    <h1>This is a sample template file.</h1>
</body>
</html>
```

## Views in Django
### Sample Function-Based Views
A function-based view:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a function based view.")
```

### Sample Class-Based Views
A class-based view:

```python
from django.views import View

class SimpleClassBasedView(View):
    def get(self, request):
        pass  # Code to process a GET request
```

## URLs in Django
Define URL patterns to be matched against the requested URL.

### Sample urls.py Files
File 1:

```python
from django.contrib import admin
from django.urls import path
from . import views

urlPatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
```

File 2:

```python
from django.urls import include, path

urlpatterns = [
    # ... snip ...
    path('community/', include('aggregator.urls')),
    path('contact/', include('contact.urls')),
    # ... snip ...
]
```

## Forms in Django
Forms are created by Django using the form field.

### Sample Django Form
```python
from django import forms

class SampleForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
```

## Apps in Django
Apps are like independent modules for different functionalities.

### Creating an App
Create a new app:

```bash
python manage.py startapp AppName
```

### Listing App in settings.py
Add the app name to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AppName'
]
```

## Templates in Django
Templates handle dynamic HTML files separately.

### Configuring Templates in settings.py
Configure templates in `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            # some options here
        },
    },
]
```

### Changing views.py File
Update the view to use a template:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

### Sample Template File
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Template is working</title>
</head>
<body>
    <h1>This is a sample Django template.</h1>
</body>
</html>
```

## Migrations in Django
Migrations are used to update the database schema based on model changes.

### Creating a Migration
Create migration files:

```bash
python manage.py makemigrations
```

### Applying the Migration
Apply changes to the actual database:

```bash
python manage.py migrate
```

## Admin Interface in Django
Django provides a ready-to-use admin interface.

### Creating Admin User
Create an admin user:

```bash
python manage.py createsuperuser
```

## Page Redirection
Redirect users to a specific page on an event.

### Redirect Method
```python
from django.shortcuts import render, redirect

def redirecting(request):
    return redirect("https://www.codesWithpankaj.com")
```

---

Feel free to explore more features and functionalities of Django in the official documentation: [Django Documentation](https://docs.djangoproject.com/).