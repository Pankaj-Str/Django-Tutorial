# Django Add Master Template

Adding a master template, often referred to as a base template, is a good practice in Django for creating a consistent layout across multiple pages. This involves creating a base HTML template that contains the common structure, such as header, footer, and navigation, and then extending this base template in other templates.

Here's how you can add a master template to your Django project:

### 1. Create a Base Template:

Create a new HTML file, let's call it `base.html`, in your `templates` folder. This file will serve as the base template for your project.

```html
<!-- my_tennis_club/templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Tennis Club{% endblock %}</title>
</head>
<body>

<header>
    <h1>My Tennis Club</h1>
    <!-- Add navigation, menu, or other common elements here -->
</header>

<main>
    {% block content %}{% endblock %}
</main>

<footer>
    <!-- Add footer content here -->
</footer>

</body>
</html>
```

In this template, `{% block title %}` and `{% block content %}` are placeholders for the specific title and content of each page. You'll replace them in the templates that extend this base template.

### 2. Update the Members Template:

Modify your `all_members.html` template to extend the `base.html` template:

```html
<!-- my_tennis_club/members/templates/all_members.html -->

{% extends 'base.html' %}

{% block content %}

<h1>Members</h1>
  
<ul>
  {% for member in mymembers %}
    <li>
      <a href="{% url 'member-details' member.id %}">
        {{ member.firstname }} {{ member.lastname }}
      </a>
    </li>
  {% endfor %}
</ul>

{% endblock %}
```

In this template, `{% extends 'base.html' %}` tells Django that this template extends the `base.html` template. The `{% block content %}` and `{% endblock %}` tags define the specific content for this page.

### 3. Update the Member Details Template:

Similarly, update your `member_details.html` template to extend the `base.html` template:

```html
<!-- my_tennis_club/members/templates/member_details.html -->

{% extends 'base.html' %}

{% block content %}

<h1>Member Details</h1>

<p>Name: {{ member.firstname }} {{ member.lastname }}</p>
<p>Email: {{ member.email }}</p>
<!-- Add more details as needed -->

{% endblock %}
```

### 4. Run the Development Server:

Run the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/myapp/members/` and `http://127.0.0.1:8000/myapp/members/1/` in your browser. You should see the common layout from the `base.html` template applied to both pages.

This approach helps maintain a consistent design across your site and simplifies updates to the shared elements of your pages. Adjust the template names and paths according to your project's structure and requirements.
