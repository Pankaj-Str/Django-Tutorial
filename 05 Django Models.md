# Django Models


### Create a Django Project and App with User Profiles

#### Step 1: Create a Django Project

1.1 Open your terminal or command prompt.

1.2 Navigate to the desired directory where you want to create your project.

1.3 Run the following command to create a new Django project named `p4n_profiles`:

```bash
django-admin startproject p4n_profiles
```

1.4 Change into the project directory:

```bash
cd p4n_profiles
```

#### Step 2: Create a Django App

2.1 Inside the `p4n_profiles` project directory, run the following command to create a new Django app named `members`:

```bash
python manage.py startapp members
```

#### Step 3: Add App to `INSTALLED_APPS`

3.1 Open the `settings.py` file inside the `p4n_profiles` project directory.

3.2 Locate the `INSTALLED_APPS` list and add `'members'` to it:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members',
]
```

#### Step 4: Define a Model

4.1 Open the `models.py` file inside the `members` app.

4.2 Import necessary modules:

```python
from django.db import models
```

4.3 Define a simple `UserProfile` model with fields such as `first_name`, `last_name`, and `email`:

```python
class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```

#### Step 5: Make Migrations

5.1 Open your terminal in the project directory (`p4n_profiles`).

5.2 Run the following command to create migrations based on your model changes:

```bash
python manage.py makemigrations
```

5.3 Apply the migrations:

```bash
python manage.py migrate
```

#### Step 6: Run Initial Server

6.1 Start the development server:

```bash
python manage.py runserver
```

6.2 Open your web browser and go to `127.0.0.1:8000` to check if the project is running.

#### Step 7: Create Views

7.1 Open the `views.py` file in the `members` app.

7.2 Use the `UserProfile` model in your views to interact with the database. For example, you can query and display user profiles:

```python
from django.shortcuts import render
from .models import UserProfile

def display_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'members/profile_list.html', {'profiles': profiles})
```

#### Step 8: Create Templates

8.1 Create a new folder named `templates` inside the `members` app.

8.2 Inside the `templates` folder, create a new HTML file named `profile_list.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>User Profiles</title>
</head>
<body>

<div class="container mt-4">
    <h1>User Profiles</h1>

    <table class="table">
        <thead>
        <tr>
            <th scope="col">First Name</th>
            <th scope="col">Last Name</th>
            <th scope="col">Email</th>
        </tr>
        </thead>
        <tbody>
        {% for profile in profiles %}
            <tr>
                <td>{{ profile.first_name }}</td>
                <td>{{ profile.last_name }}</td>
                <td>{{ profile.email }}</td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
</div>

<!-- Bootstrap JS, Popper.js, and jQuery (required for Bootstrap) -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
        integrity="sha384-EeGoh0OM4gNX7Vl+kcZdI2wfcJSctOdhlT5q5Z5ePSSZcxWnuPij8me7z9eCrPU"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgydRHTZX7Ii+vwzgzmveE/QpDYDAtWT1B9t0d7h/6i6U/m6fTqvi2utmjpP"
        crossorigin="anonymous"></script>

</body>
</html>

```

#### Step 9: Create Superuser

9.1 Run the following command to create a superuser:

```bash
python manage.py createsuperuser
```

9.2 Follow the prompts to enter a username, email, and password for the superuser.

9.3 Use the superuser credentials to log in to the Django admin panel at `127.0.0.1:8000/admin/`.

#### Step 10: Update URLs

10.1 Create a `urls.py` file inside the `members` app.

10.2 Define a URL pattern to link to the `display_profiles` view:

```python
from django.urls import path
from .views import display_profiles

urlpatterns = [
    path('profiles/', display_profiles, name='profile_list'),
]
```

10.3 Configure project URLs by updating the `urls.py` file in the `p4n_profiles` project:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
]
```

#### Step 11: Run Server and View Profiles

11.1 Start the development server:

```bash
python manage.py runserver
```

11.2 Open your web browser and go to `127.0.0.1:8000/members/profiles/` to view the user profiles.

By following these steps, you should have successfully created a Django project
