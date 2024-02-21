# Template Inheritance/ Template Extending

Template inheritance, also known as template extending, is a powerful feature in Django that allows you to create a base template containing common elements and structure, and then extend it in other templates to override specific blocks or add additional content. Here's how template inheritance works in Django:

### Base Template:

1. **Create a Base Template**: Create a base template that contains the common structure and elements shared across multiple pages of your website.

```html
<!-- base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Welcome to My Site</h1>
        <!-- Common header content goes here -->
    </header>

    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/contact/">Contact</a></li>
        </ul>
    </nav>

    <main>
        {% block content %}
        <!-- Default content goes here -->
        {% endblock %}
    </main>

    <footer>
        <!-- Common footer content goes here -->
    </footer>
</body>
</html>
```

### Child Templates:

2. **Extend the Base Template**: In other templates, extend the base template and override specific blocks as needed or add additional content.

```html
<!-- home.html -->

{% extends 'base.html' %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
<h2>Welcome to the Home Page</h2>
<p>This is the content of the home page.</p>
{% endblock %}
```

```html
<!-- about.html -->

{% extends 'base.html' %}

{% block title %}About - My Site{% endblock %}

{% block content %}
<h2>About Us</h2>
<p>This is the content of the About Us page.</p>
{% endblock %}
```

```html
<!-- contact.html -->

{% extends 'base.html' %}

{% block title %}Contact - My Site{% endblock %}

{% block content %}
<h2>Contact Us</h2>
<p>This is the content of the Contact Us page.</p>
{% endblock %}
```

### Explanation:

- `{% extends 'base.html' %}`: Instructs Django to extend the specified base template.
- `{% block %}` tags: Define blocks within the base template that can be overridden in child templates.
- `{% block title %}`, `{% block content %}`: Blocks that can be overridden in child templates to customize the title and content of each page.

### Benefits:

- Promotes code reusability by defining common elements in a single location (the base template).
- Allows for easy customization and maintenance of individual pages.
- Provides a clear and organized structure for your templates.

By using template inheritance, you can create a consistent layout for your website while still allowing for flexibility and customization on a per-page basis.