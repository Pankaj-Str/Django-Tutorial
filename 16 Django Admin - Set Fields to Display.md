# Django Admin - Set Fields to Display

In Django Admin, you can customize the fields that are displayed for each model in the list view by using the `list_display` option in the corresponding `ModelAdmin` class. This allows you to control which fields are shown for each record in the list.

Here's how you can set the fields to display for the `Member` model in the Django Admin:

### 1. Update `admin.py`:

In the `admin.py` file of your app (`myapp` in this example), create or update the `ModelAdmin` class for the `Member` model. Use the `list_display` option to specify the fields you want to display in the list view:

```python
# admin.py in myapp

from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')  # Specify the fields to display

admin.site.register(Member, MemberAdmin)
```

In this example, the `list_display` option is set to a tuple of field names ('firstname', 'lastname', 'email'). This will display these fields for each `Member` instance in the Django Admin list view.

### 2. Run the Development Server:

Ensure your development server is running:

```bash
python manage.py runserver
```

### 3. Access the Django Admin Interface:

Visit `http://127.0.0.1:8000/admin/` in your browser and log in with the superuser credentials.

### 4. Navigate to the Members Section:

In the Django Admin interface, go to the "Members" section under the "myapp" app (or your app name).

### 5. View Members List:

You should now see a list of members with the specified fields displayed.

By customizing the `list_display` option in the `ModelAdmin` class, you can choose which fields to show in the list view, making it more tailored to your needs.

Feel free to adjust the field names in the `list_display` tuple according to your `Member` model's structure and your preferences.
