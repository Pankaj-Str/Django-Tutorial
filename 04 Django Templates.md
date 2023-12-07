# Django Templates

Django templates are used to generate HTML dynamically in your web applications. They allow you to embed variables, control structures, and template tags within HTML files. Here's an overview of how Django templates work:

### Template Structure:

1. **Create a Templates Directory:**
   In each Django app, you should have a `templates` directory to store your HTML templates. Django will look for templates within this directory.

   ```plaintext
   myapp/
   ├── templates/
   │   └── myapp/
   │       └── index.html
   └── ...
   ```

   In the example above, there's a `templates` directory inside the `myapp` directory, and the template file is named `index.html`.

### Embedding Variables:

2. **Embed Variables in Templates:**
   In your HTML templates, you can embed variables using double curly braces `{{ variable_name }}`. For example:

   ```html
   <!-- templates/myapp/index.html -->

   <h1>{{ title }}</h1>
   <p>{{ content }}</p>
   ```

   In this example, `title` and `content` are variables that will be passed from the Django view.

### Control Structures:

3. **Use Control Structures:**
   Django templates support control structures such as `if`, `for`, and `block`. For example:

   ```html
   <!-- templates/myapp/index.html -->

   {% if user.is_authenticated %}
       <p>Welcome, {{ user.username }}!</p>
   {% else %}
       <p>Please log in.</p>
   {% endif %}
   ```

   In this example, the template checks if the user is authenticated and displays a personalized message accordingly.

### Template Tags:

4. **Use Template Tags:**
   Django provides template tags enclosed in `{% %}` for more complex logic. For example:

   ```html
   <!-- templates/myapp/index.html -->

   <ul>
       {% for item in items %}
           <li>{{ item }}</li>
       {% endfor %}
   </ul>
   ```

   Here, the template iterates through a list of items and generates an HTML list.

### Include Templates:

5. **Include Templates:**
   You can include other templates using the `{% include %}` tag. For example:

   ```html
   <!-- templates/myapp/base.html -->

   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>{% block title %}My Site{% endblock %}</title>
   </head>
   <body>
       {% block content %}{% endblock %}
   </body>
   </html>
   ```

   In this example, the `base.html` template includes blocks (`{% block %}`) that can be overridden in other templates that extend it.

### Template Inheritance:

6. **Use Template Inheritance:**
   Templates can inherit from a base template using the `{% extends %}` tag. For example:

   ```html
   <!-- templates/myapp/index.html -->

   {% extends 'myapp/base.html' %}

   {% block title %}Home{% endblock %}

   {% block content %}
       <h1>Welcome to my site!</h1>
   {% endblock %}
   ```

   In this case, `index.html` extends the `base.html` template and overrides the title and content blocks.

### Static Files:

7. **Handle Static Files:**
   To include static files (CSS, JavaScript, images), use the `{% static %}` tag. For example:

   ```html
   <!-- templates/myapp/index.html -->

   <link rel="stylesheet" href="{% static 'css/style.css' %}">
   ```

   Make sure to configure your project to handle static files properly, including setting up the `STATICFILES_DIRS` and using the `{% load static %}` tag at the top of your template.

These are just a few examples of what you can do with Django templates. They provide a powerful and flexible way to generate dynamic HTML content in your web applications.
