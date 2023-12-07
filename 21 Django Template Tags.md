# Django Template Tags 
Django template tags are enclosed within curly braces with percent signs (`{% %}`) and are used to embed control structures or logic within Django templates. Here's an overview of some commonly used Django template tags:

### 1. If-Else:

```html
{% if condition %}
    <!-- Code to execute if condition is True -->
{% else %}
    <!-- Code to execute if condition is False -->
{% endif %}
```

### 2. For Loop:

```html
{% for item in items %}
    <!-- Code to repeat for each item in the iterable -->
{% endfor %}
```

### 3. Block and Extends:

Inheritance is achieved using `{% block %}`, `{% extends %}`, and `{% include %}`.

In the base template (`base.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

In a child template:

```html
{% extends 'base.html' %}

{% block title %}My Custom Title{% endblock %}

{% block content %}
    <!-- Custom content for this page -->
{% endblock %}
```

### 4. Include:

Include another template in the current one using `{% include %}`.

```html
{% include 'header.html' %}
```

### 5. URL:

Generate URLs using the `{% url %}` tag.

```html
<a href="{% url 'my_view_name' arg1=value1 %}">Link Text</a>
```

### 6. CSRF Token:

Include the CSRF token in forms.

```html
{% csrf_token %}
```

### 7. Comments:

Add comments to your templates.

```html
{# This is a comment #}
```

### 8. Filters:

Use filters to modify variable output.

```html
{{ variable|filter_name }}
```

### 9. With:

Assign a new variable within a block.

```html
{% with total=product.price * quantity %}
    Total: ${{ total }}
{% endwith %}
```

These are just some of the many template tags available in Django. Django's template language is quite powerful and flexible, allowing you to create dynamic and reusable templates for your web applications. For more details and a complete list of template tags, you can refer to the official Django documentation on [template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/).
