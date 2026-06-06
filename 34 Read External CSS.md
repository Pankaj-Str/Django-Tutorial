# How to Read External CSS in Django

In Django, CSS files are stored inside the **static** folder. Django serves these files using the **static files system**.

---

# Step 1: Create a Django Project

```bash
django-admin startproject myproject
cd myproject
```

Create an app:

```bash
python manage.py startapp website
```

Add the app to `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]
```

---

# Step 2: Configure Static Files

Open `settings.py`:

```python
STATIC_URL = 'static/'
```

For development, this is usually enough.

---

# Step 3: Create Static Folder Structure

Inside your app, create the following folders:

```text
website/
│
├── static/
│   └── website/
│       └── css/
│           └── style.css
│
├── templates/
│   └── home.html
│
├── views.py
```

---

# Step 4: Create CSS File

**website/static/website/css/style.css**

```css
body {
    background-color: lightblue;
    font-family: Arial, sans-serif;
}

h1 {
    color: darkblue;
    text-align: center;
}

p {
    color: green;
    font-size: 20px;
}
```

---

# Step 5: Create HTML Template

**website/templates/home.html**

First load static files:

```html
{% load static %}
```

Link the CSS file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django CSS Example</title>

    <link rel="stylesheet" href="{% static 'website/css/style.css' %}">
</head>
<body>

    <h1>Welcome to Django</h1>

    <p>This page is using an external CSS file.</p>

</body>
</html>
```

---

# Step 6: Create View

**views.py**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

---

# Step 7: Create URL for App

Create `website/urls.py`

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

---

# Step 8: Include App URLs in Project

Open `myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
```

---

# Step 9: Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

You should see:

* Light blue background
* Blue heading
* Green paragraph text

---

# Common Mistakes

### 1. Forgot to load static

Wrong:

```html
<link rel="stylesheet" href="{% static 'website/css/style.css' %}">
```

Correct:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'website/css/style.css' %}">
```

---

### 2. Wrong CSS Path

Wrong:

```html
{% static 'css/style.css' %}
```

Correct:

```html
{% static 'website/css/style.css' %}
```

---

### 3. CSS File Not Inside Static Folder

Correct structure:

```text
website/
└── static/
    └── website/
        └── css/
            └── style.css
```

---

# Complete Example

### style.css

```css
body{
    background-color:#f4f4f4;
}

h1{
    color:red;
}
```

### home.html

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <title>CSS Demo</title>

    <link rel="stylesheet" href="{% static 'website/css/style.css' %}">
</head>
<body>

<h1>Hello Django</h1>

</body>
</html>
```

Output:

```text
Hello Django
```

The heading will appear in **red color**, proving that Django successfully loaded the external CSS file.
