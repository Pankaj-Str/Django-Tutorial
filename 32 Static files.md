# Static files

Static files in Django typically include CSS, JavaScript, images, and other assets that are served directly to the client without modification by the server. Here's how you can work with static files in a Django project:

### Setting Up Static Files:

1. **Create a Static Directory**: Within your Django app's directory, create a directory named `static` to store your static files.

```bash
mkdir myapp/static
```

2. **Place Your Static Files**: Place your static files (CSS, JavaScript, images, etc.) inside the `static` directory. You can organize them into subdirectories if needed.

```bash
myapp/static/
├── css/
│   └── styles.css
├── js/
│   └── script.js
└── img/
    └── logo.png
```

### Serving Static Files Locally (Development):

1. **Configure Static Files Settings**: In your Django project's settings file (`settings.py`), make sure the `STATIC_URL` setting is defined.

```python
# settings.py

STATIC_URL = '/static/'
```

2. **Load Static Files in Templates**: Load static files in your templates using the `{% static %}` template tag.

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
</head>
<body>
    <img src="{% static 'img/logo.png' %}" alt="Logo">
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

### Serving Static Files in Production:

In a production environment, it's common to use a web server like Nginx or Apache to serve static files. Django itself can also serve static files in production, but it's not recommended for high-traffic sites. Instead, you can use a separate service like AWS S3 or a CDN (Content Delivery Network) for better performance and scalability.

1. **Configure Static Files Settings for Production**: In `settings.py`, set the `STATIC_ROOT` setting to define where Django should collect static files for deployment.

```python
# settings.py

STATIC_URL = '/static/'
STATIC_ROOT = '/path/to/your/static/directory/'
```

2. **Collect Static Files**: Run the `collectstatic` management command to collect static files from all your apps into the `STATIC_ROOT` directory.

```bash
python manage.py collectstatic
```

3. **Serve Static Files with a Web Server**: Configure your web server to serve static files from the `STATIC_ROOT` directory. You may need to set up a separate location or alias in your web server's configuration file.

### Using Static Files in Views:

In Django views, you can use the `static()` function to generate the URL for static files.

```python
from django.templatetags.static import static

def my_view(request):
    css_url = static('css/styles.css')
    # Do something with the CSS URL
```

By following these steps, you can effectively manage and serve static files in your Django project, both in development and production environments.