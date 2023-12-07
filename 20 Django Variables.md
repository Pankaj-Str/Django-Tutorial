# Django Variables

In Django templates, variables are used to display dynamic content. Variables are enclosed within double curly braces (`{{ }}`). Here's a brief overview of using variables in Django templates:

### Example:

Assume you have a Django view that passes a variable `username` to a template:

```python
# views.py
from django.shortcuts import render

def my_view(request):
    username = "John"
    return render(request, 'my_template.html', {'username': username})
```

In the template (`my_template.html`), you can use the `{{ username }}` variable to display its value:

```html
<!-- my_template.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome, {{ username }}!</h1>
</body>
</html>
```

In this example, when the template is rendered, the content of the `username` variable from the view will replace `{{ username }}`. So, if `username` is "John," the rendered HTML will be:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome, John!</h1>
</body>
</html>
```

### Dynamic Data:

Variables are commonly used to display dynamic data from the context passed by the views. They can represent any data type, including strings, numbers, lists, dictionaries, or more complex objects.

```python
# views.py
from django.shortcuts import render

def my_view(request):
    context = {
        'name': 'Alice',
        'age': 25,
        'colors': ['red', 'green', 'blue'],
    }
    return render(request, 'my_template.html', context)
```

```html
<!-- my_template.html -->
<!DOCTYPE html>
<html>
<head>
    <title>User Info</title>
</head>
<body>
    <h1>{{ name }}'s Profile</h1>
    <p>Age: {{ age }}</p>
    
    <h2>Favorite Colors:</h2>
    <ul>
        {% for color in colors %}
            <li>{{ color }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

In this example, the template displays the user's name, age, and a list of favorite colors.

### Filters:

You can also use filters with variables to modify their display. For example:

```html
<!-- Uppercase the username -->
<p>{{ username|upper }}</p>

<!-- Format a date -->
<p>{{ date_created|date:"F j, Y" }}</p>
```

Django provides various built-in filters to manipulate the display of variables.
