# Django include Tag

The `{% include %}` tag in Django allows you to include the contents of another template within your current template. This is useful for reusing common elements across multiple templates without duplicating code. Here's how you can use the `{% include %}` tag:

1. **Create a Reusable Template**: First, create a template that you want to include in other templates. For example, let's create a template for the header of your site.

```html
<!-- myapp/templates/header.html -->

<header>
    <h1>Welcome to My Site</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/contact/">Contact</a></li>
        </ul>
    </nav>
</header>
```

2. **Include the Template**: Now, you can include this header template in your `base.html` template or any other template where you want the header to appear.

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
    {% include 'header.html' %}

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

In this example, `{% include 'header.html' %}` includes the contents of the `header.html` template within the `base.html` template.

3. **Create Specific Templates**: You can create specific templates for different pages of your site, and they will inherit the header included from the `base.html` template.

```html
<!-- myapp/templates/home.html -->

{% extends 'base.html' %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
<h2>Welcome to the Home Page</h2>
<p>This is the content of the home page.</p>
{% endblock %}
```

4. **Configure Template Settings**: Ensure that your project's settings are configured to look for templates in your app's directory, as mentioned in the previous answer.

That's it! Now, when you render a template that extends the `base.html` template, it will include the header content from the `header.html` template. This approach keeps your code DRY (Don't Repeat Yourself) and makes it easier to maintain. It's particularly useful for including common elements like headers, footers, or sidebars across multiple pages.
