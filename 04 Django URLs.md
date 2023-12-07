# Django URLs

In Django, the URL patterns are defined in the `urls.py` files. These files are used to map URLs to views, allowing you to specify how different URLs should be handled by your Django application. Here's an overview of how Django URLs work:

### Project-level URLs:

1. **Create a URLs File:**
   In your Django project, you typically have a main `urls.py` file in the project directory (next to the `settings.py` file). This file is responsible for including URLs from various apps.

   ```python
   # projectname/urls.py

   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('myapp/', include('myapp.urls')),  # Include app-specific URLs
   ]
   ```

   In the example above, URLs matching the pattern `/myapp/` are delegated to the `urls.py` file of the `myapp` app.

### App-level URLs:

2. **Create URLs for Each App:**
   Each app in your Django project should have its own `urls.py` file to define the URL patterns specific to that app.

   ```python
   # myapp/urls.py

   from django.urls import path
   from . import views

   urlpatterns = [
       path('my-view/', views.my_view, name='my-view'),
       # Additional URL patterns for the app
   ]
   ```

   Here, the URL `/myapp/my-view/` is mapped to the `my_view` function in the `views.py` file of the `myapp` app.

### Including App URLs in the Project URLs:

3. **Include App URLs in Project URLs:**
   Make sure to include the app-specific URLs in the project-level `urls.py` file using the `include` function.

   ```python
   # projectname/urls.py

   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('myapp/', include('myapp.urls')),  # Include app-specific URLs
   ]
   ```

   This allows you to organize your project URLs in a modular way, with each app defining its own URLs.

### Regular Expressions in URL Patterns:

4. **Use Regular Expressions (Optional):**
   Django's `path` function allows you to use regular expressions in URL patterns. For example:

   ```python
   # myapp/urls.py

   from django.urls import path
   from . import views

   urlpatterns = [
       path('articles/<int:article_id>/', views.article_detail, name='article-detail'),
   ]
   ```

   In this case, `<int:article_id>` captures an integer value from the URL, which is then passed as an argument to the associated view function.

### Namespace URLs (Optional):

5. **Use URL Namespaces (Optional):**
   You can namespace your app URLs to avoid naming conflicts between different apps.

   ```python
   # myapp/urls.py

   from django.urls import path
   from . import views

   app_name = 'myapp'  # Namespace for the app

   urlpatterns = [
       path('my-view/', views.my_view, name='my-view'),
   ]
   ```

   In the project-level `urls.py` file, include the app URLs with the namespace:

   ```python
   # projectname/urls.py

   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('myapp/', include('myapp.urls', namespace='myapp')),  # Include app-specific URLs with namespace
   ]
   ```

   This can be useful when you have similar URL patterns in different apps.

