# Django include Tag

In Django templates, the `{% include %}` tag is used to include the contents of another template within the current one. This feature allows you to create modular and reusable templates. Here's the basic syntax:

```html
{% include 'template_name.html' %}
```

### Example:

Let's say you have a header template (`header.html`):

```html
<!-- header.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>{% block header %}Welcome{% endblock %}</h1>
    </header>
```

And a footer template (`footer.html`):

```html
<!-- footer.html -->
    <footer>
        <p>&copy; 2023 My Site</p>
    </footer>
</body>
</html>
```

You can then include these templates in another template (`main_template.html`):

```html
<!-- main_template.html -->
{% include 'header.html' %}

{% block content %}
    <!-- Main content goes here -->
{% endblock %}

{% include 'footer.html' %}
```

In this example, the `{% include 'header.html' %}` and `{% include 'footer.html' %}` tags include the contents of the `header.html` and `footer.html` templates respectively. The `{% block %}` tags in the included templates allow for flexibility, enabling you to override specific content in the including template.

### Passing Variables to Included Templates:

You can also pass variables to the included templates by using the `with` option:

```html
{% include 'header.html' with title='My Custom Title' %}
```

In the `header.html` template, you can then use the `title` variable:

```html
<!-- header.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <header>
        <h1>{% block header %}Welcome{% endblock %}</h1>
    </header>
```

This allows you to customize the included template based on the context of the including template.

Django's `{% include %}` tag promotes code reusability by allowing you to break down your templates into smaller, modular components. It's particularly useful for including common elements like headers, footers, or sidebars across multiple pages.
