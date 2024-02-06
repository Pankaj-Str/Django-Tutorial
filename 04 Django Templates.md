# Template

### Step 1: Create a Django Project

1.1 Open your terminal or command prompt.

1.2 Navigate to the desired directory where you want to create your project.

1.3 Run the following command to create a new Django project named `p4n`:

```bash
django-admin startproject p4n
```

1.4 Change into the project directory:

```bash
cd p4n
```

### Step 2: Create an App and Template

2.1 Inside the `p4n` project directory, run the following command to create a new Django app named `members`:

```bash
python manage.py startapp members
```

2.2 Open the `members` folder and create a `templates` folder inside it.

2.3 Inside the `templates` folder, create an HTML file named `myfirst.html`.

2.4 Open `myfirst.html` and insert the following HTML code:

```html
<!DOCTYPE html>
<html>
<body>

<h1>Hello World!</h1>
<p>Welcome to my first Django project!</p>

</body>
</html>
```

### Step 3: Modify the View

3.1 Open the `views.py` file inside the `members` folder.

3.2 Replace the existing `members` view with the following code:

```python
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
```

### Step 4: Change Settings

4.1 Open the `settings.py` file inside the `p4n` folder.

4.2 Locate the `INSTALLED_APPS` list and add `'members'` to it:

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

### Step 5: Run Migrations

5.1 In the terminal, while in the `p4n` project directory, run the following command to apply migrations:

```bash
python manage.py migrate
```

### Step 6: Start the Development Server

6.1 In the same terminal, while in the `p4n` project directory, start the development server with the following command:

```bash
python manage.py runserver
```

### Step 7: View the Template in Your Browser

7.1 Open your web browser and type `127.0.0.1:8000/members/` in the address bar.

Congratulations! You've successfully created a Django project named `p4n` with a simple template. Feel free to explore more features and build upon this foundation for your Django application.
