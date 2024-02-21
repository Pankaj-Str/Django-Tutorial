# Pass Arguments with Include

In Django, you can pass arguments to included templates using the `{% include %}` tag by specifying them in the form of key-value pairs. These arguments can then be accessed within the included template. Here's how you can pass arguments with the `{% include %}` tag:

1. **Create a Reusable Template with Arguments**: Let's create a modified version of the header template (`header.html`) that accepts an argument for the website title.

```html
<!-- myapp/templates/header.html -->

<header>
    <h1>{{ title }}</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/contact/">Contact</a></li>
        </ul>
    </nav>
</header>
```

2. **Include the Template with Arguments**: Now, include the modified `header.html` template in your `base.html` template and pass the title as an argument.

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
    {% include 'header.html' with title="My Site" %}

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

In this example, `{% include 'header.html' with title="My Site" %}` includes the `header.html` template and passes the argument `title` with the value `"My Site"`.

3. **Access the Argument in the Included Template**: Within the `header.html` template, you can access the passed argument using the specified key, in this case, `title`.

```html
<!-- myapp/templates/header.html -->

<header>
    <h1>{{ title }}</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/contact/">Contact</a></li>
        </ul>
    </nav>
</header>
```

4. **Configure Template Settings**: Ensure that your project's settings are configured to look for templates in your app's directory, as mentioned in the previous answers.

That's it! Now, when you render a template that extends the `base.html` template, it will include the header content from the `header.html` template with the specified title argument. This approach allows you to customize the included templates based on the context in which they are included.