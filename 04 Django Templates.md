# Template

In Django, a base template serves as the foundation for other templates in your project. It typically contains the common structure, layout, and elements that are shared across multiple pages of your website or web application. Creating a base template helps in maintaining consistency and reduces redundancy in your code.

Here's a step-by-step guide to creating a Django base template:

1. **Create a Django Project**: If you haven't already, create a new Django project using the `django-admin` command-line tool.

```bash
django-admin startproject myproject
```

2. **Create an App**: Inside your project, create a new Django app using the following command:

```bash
python manage.py startapp myapp
```

3. **Create a Templates Directory**: Inside your app directory (`myapp`), create a directory named `templates`. This is where Django will look for template files.

```bash
mkdir myapp/templates
```

4. **Create the Base Template File**: Inside the `templates` directory, create a file named `base.html`. This will be your base template.

```html
<!-- myapp/templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <!-- Header content goes here -->
    </header>

    <nav>
        <!-- Navigation menu goes here -->
    </nav>

    <main>
        {% block content %}
        <!-- Default content goes here -->
        {% endblock %}
    </main>

    <footer>
        <!-- Footer content goes here -->
    </footer>
</body>
</html>
```

In the above code:
- `{% block title %}My Site{% endblock %}` defines a block named `title`. This allows child templates to override the title of the page.
- `{% block content %}` and `{% endblock %}` define a block named `content`. Child templates can override this block with their own content.

5. **Extend the Base Template**: Now, you can create other templates that extend the base template. For example, let's create a template for the home page.

```html
<!-- myapp/templates/home.html -->

{% extends 'base.html' %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
<h1>Welcome to My Site</h1>
<p>This is the home page content.</p>
{% endblock %}
```

In this template, `{% extends 'base.html' %}` indicates that this template extends the `base.html` template. It overrides the `title` block with "Home - My Site" and the `content` block with custom content for the home page.

6. **Configure Template Settings**: Finally, make sure your project's settings are configured to look for templates in your app. Open the `settings.py` file in your Django project and add the following line:

```python
# myproject/settings.py

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates')],
        ...
    },
]
```

Replace `'myapp'` with the name of your app.

That's it! You've now created a base template in Django and extended it to create a specific template for the home page. You can repeat the process to create other templates that inherit from the base template.

### Step 7: View the Template in Your Browser

7.1 Open your web browser and type `127.0.0.1:8000/members/` in the address bar.

Congratulations! You've successfully created a Django project named `p4n` with a simple template. Feel free to explore more features and build upon this foundation for your Django application.
