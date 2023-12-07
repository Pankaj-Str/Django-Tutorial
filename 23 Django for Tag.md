# Django for Tag 

In Django templates, the `{% for %}` and `{% endfor %}` tags are used to create loops. You can use them to iterate over elements in a list, dictionary, queryset, or any other iterable object. Here's the basic syntax:

```html
{% for item in iterable %}
    <!-- Code to repeat for each item in the iterable -->
{% endfor %}
```

### Example:

Assuming you have a list of items in your context:

```python
# views.py
from django.shortcuts import render

def my_view(request):
    items = ['Apple', 'Banana', 'Orange', 'Grapes']
    return render(request, 'my_template.html', {'items': items})
```

In your template (`my_template.html`), you can use the `{% for %}` tag to iterate over the list and display each item:

```html
<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

This will generate an unordered list (`<ul>`) with list items (`<li>`) for each item in the `items` list.

### Loop Variables:

Django provides loop variables that you can use within the loop:

- `forloop.counter`: The current iteration of the loop (1-indexed).
- `forloop.counter0`: The current iteration of the loop (0-indexed).
- `forloop.first`: True if this is the first iteration.
- `forloop.last`: True if this is the last iteration.

For example:

```html
<ul>
    {% for item in items %}
        <li>{{ forloop.counter }}. {{ item }}</li>
    {% endfor %}
</ul>
```

This will display the items with their corresponding iteration numbers.

### Nested Loops:

You can also have nested `{% for %}` loops to iterate over nested data structures:

```python
# views.py
from django.shortcuts import render

def my_view(request):
    data = {'fruits': ['Apple', 'Banana'], 'vegetables': ['Carrot', 'Broccoli']}
    return render(request, 'my_template.html', {'data': data})
```

```html
<ul>
    {% for category, items in data.items %}
        <li>{{ category }}
            <ul>
                {% for item in items %}
                    <li>{{ item }}</li>
                {% endfor %}
            </ul>
        </li>
    {% endfor %}
</ul>
```

This will generate a nested list with categories and items.

Django's `{% for %}` tag provides a flexible and powerful way to iterate over data in your templates. It's commonly used when rendering dynamic content, such as displaying items in a list, table, or dropdown.
