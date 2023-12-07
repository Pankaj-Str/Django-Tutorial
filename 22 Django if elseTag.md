# Django if elseTag 

In Django templates, the `{% if %}` and `{% else %}` tags are used to create conditional statements. Here's how you can use the `{% if %}` and `{% else %}` tags in Django:

```html
{% if condition %}
    <!-- Code to execute if the condition is True -->
{% else %}
    <!-- Code to execute if the condition is False -->
{% endif %}
```

### Example:

Let's say you have a variable `is_authenticated` in your context:

```python
# views.py
from django.shortcuts import render

def my_view(request):
    is_authenticated = request.user.is_authenticated
    return render(request, 'my_template.html', {'is_authenticated': is_authenticated})
```

In your template (`my_template.html`), you can use the `{% if %}` and `{% else %}` tags to conditionally display content:

```html
{% if is_authenticated %}
    <p>Welcome, {{ request.user.username }}!</p>
{% else %}
    <p>Please log in</p>
{% endif %}
```

In this example, if the user is authenticated (`is_authenticated` is True), it will display a welcome message with the username. Otherwise, it will display a message prompting the user to log in.

### Checking for the Existence of a Variable:

You can also use the `{% if %}` tag to check if a variable exists before using it. For example:

```html
{% if some_variable %}
    <p>The variable exists and is not empty.</p>
{% else %}
    <p>The variable does not exist or is empty.</p>
{% endif %}
```

This can be useful to avoid errors when trying to access properties or attributes of variables that might be `None` or not defined.

### Complex Conditions:

You can include more complex conditions using logical operators (`and`, `or`, `not`) and comparisons:

```html
{% if age > 18 and country == 'USA' %}
    <p>You are eligible to vote in the USA.</p>
{% else %}
    <p>You are not eligible to vote in the USA.</p>
{% endif %}
```

Django's template language provides flexibility in constructing conditional statements to control the rendering of content based on various conditions.
