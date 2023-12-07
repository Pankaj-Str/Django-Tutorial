# Django Admin - Include Member

To include the `Member` model in Django Admin, you need to register it in the `admin.py` file of your app. Assuming you have a `Member` model in an app named `myapp`, here are the steps:

### 1. Define the `Member` Model:

Assuming you have a `Member` model defined in `models.py`:

```python
# models.py in myapp

from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
```

### 2. Register the `Member` Model in `admin.py`:

Create or update the `admin.py` file in your `myapp` directory and register the `Member` model:

```python
# admin.py in myapp

from django.contrib import admin
from .models import Member

admin.site.register(Member)
```

### 3. Run the Development Server:

Ensure your development server is running:

```bash
python manage.py runserver
```

### 4. Access the Django Admin Interface:

Visit `http://127.0.0.1:8000/admin/` in your browser, and log in with the superuser credentials.

### 5. Navigate to the Members Section:

In the Django Admin interface, you should see a "Members" section under the "myapp" app (or whichever app you've defined your `Member` model in).

### 6. Add and Manage Members:

You can now add, edit, and delete `Member` instances using the Django Admin interface.

This process assumes you have a Django project with an app named `myapp` containing the `Member` model. Adjust the app and model names according to your project's structure.

If you have a custom user model, make sure to register it in the `admin.py` file following similar steps. The general idea is to use the `admin.site.register(Model)` function to include the models in the Django Admin interface.
