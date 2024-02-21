# Django templates

In Django templates, you can use the `{% for %}` tag along with the `forloop` object to access loop-related information such as the loop counter and cycle through a list of values. Here's how you can use `{% for %}`, `forloop.counter`, and `forloop.cycle` in Django templates:

### Using `{% for %}` Tag and `forloop.counter`:

```html
<ul>
  {% for item in items %}
    <li>{{ forloop.counter }}. {{ item }}</li>
  {% endfor %}
</ul>
```

In this example:
- `{% for item in items %}`: Starts a loop iterating over each item in the `items` list.
- `{{ forloop.counter }}`: Prints the current iteration count (1-indexed) within the loop.
- `{{ item }}`: Prints the value of the current item in the loop.

### Using `{% for %}` Tag and `forloop.cycle`:

```html
<ul>
  {% for item in items %}
    <li class="{% cycle 'odd' 'even' %}">{{ item }}</li>
  {% endfor %}
</ul>
```

In this example:
- `{% cycle 'odd' 'even' %}`: Cycles through the provided values ('odd' and 'even' in this case) on each iteration of the loop. It returns the next value in the cycle on each iteration.

### Using `forloop.counter0`:

```html
<ul>
  {% for item in items %}
    <li>{{ forloop.counter0 }}. {{ item }}</li>
  {% endfor %}
</ul>
```

In this example:
- `{{ forloop.counter0 }}`: Prints the current iteration count starting from zero (0-indexed) within the loop.

### Using `forloop.first` and `forloop.last`:

You can also use `forloop.first` and `forloop.last` to check if it's the first or last iteration of the loop:

```html
<ul>
  {% for item in items %}
    <li{% if forloop.first %} class="first"{% endif %}{% if forloop.last %} class="last"{% endif %}>{{ item }}</li>
  {% endfor %}
</ul>
```

In this example:
- `{% if forloop.first %}`: Checks if it's the first iteration of the loop.
- `{% if forloop.last %}`: Checks if it's the last iteration of the loop.
- You can apply any logic based on these conditions.

These examples demonstrate how to use loop-related variables and cycle through values in Django templates using `{% for %}`, `forloop.counter`, and `forloop.cycle`.