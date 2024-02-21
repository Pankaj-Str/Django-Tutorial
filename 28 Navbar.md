# Navbar 

Creating a navigation bar, often referred to as a navbar, is a common task in web development. In Django, you can create a reusable navbar component using templates and include it across your site's pages. Here's how you can create a simple navbar in Django:

1. **Create a Navbar Template**: First, create a template file for your navbar. You can name it something like `navbar.html`. Place it in your app's `templates` directory.

```html
<!-- myapp/templates/navbar.html -->

<nav class="navbar">
    <ul>
        <li><a href="{% url 'home' %}">Home</a></li>
        <li><a href="{% url 'about' %}">About</a></li>
        <li><a href="{% url 'contact' %}">Contact</a></li>
        <!-- Add more links as needed -->
    </ul>
</nav>
```

In this template, we're using the `{% url %}` template tag to generate URLs for the `home`, `about`, and `contact` views. Make sure you replace these with your actual view names.

2. **Include the Navbar in Your Base Template**: Next, include the navbar template in your base template (`base.html`). This will ensure that the navbar is displayed on all pages that extend the base template.

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
    {% include 'navbar.html' %}

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

3. **Style Your Navbar**: You can add CSS to style your navbar according to your design preferences. For example:

```css
/* Add your CSS styles */
.navbar {
    background-color: #333;
    padding: 10px;
}

.navbar ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

.navbar ul li {
    display: inline;
    margin-right: 10px;
}

.navbar ul li a {
    color: white;
    text-decoration: none;
}
```

4. **Configure URL Patterns**: Make sure your URL patterns are correctly defined in your `urls.py` file, as shown in previous examples.

Now, when you render a template that extends the `base.html` template, the navbar will be included at the top of the page, providing navigation links to your site's main sections. You can easily customize the navbar by modifying the `navbar.html` template and the associated CSS styles.