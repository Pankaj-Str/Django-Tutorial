# Django Add Main Index Page 

To add a main index page to your Django project, you can follow these steps:

### 1. Create a New Template:

Create a new HTML template, let's call it `index.html`, in your `templates` folder. This file will serve as the main index page.

```html
<!-- my_tennis_club/templates/index.html -->

{% extends 'base.html' %}

{% block title %}Home - My Tennis Club{% endblock %}

{% block content %}

<h1>Welcome to My Tennis Club</h1>

<p>This is the main index page. Add your main content here.</p>

{% endblock %}
```

In this template, `{% extends 'base.html' %}` indicates that this template extends the `base.html` template. The `{% block title %}` and `{% block content %}` tags define the specific title and content for this page.

### 2. Update `urls.py`:

In your app's `urls.py` file, define a new URL pattern for the main index page:

```python
# my_tennis_club/members/urls.py

from django.urls import path
from .views import members, member_details
from ..views import index  # Import the index view

urlpatterns = [
    path('', index, name='index'),  # URL for the main index page
    path('members/', members, name='all-members'),
    path('members/<int:member_id>/', member_details, name='member-details'),
]
```

### 3. Create a View:

Create a new view function for the main index page in your `views.py`:

```python
# my_tennis_club/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

### 4. Update `urls.py` in the Project Folder:

In your project's `urls.py` file, include the app-specific URLs and the URL for the main index page:

```python
# my_tennis_club/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('', index, name='index'),  # URL for the main index page
]
```

### 5. Run the Development Server:

Run the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser. You should see the main index page with the content you added to `index.html`.

This approach allows you to have a separate index page that can be accessed directly from the root URL. Adjust the template names and paths according to your project's structure and requirements.
