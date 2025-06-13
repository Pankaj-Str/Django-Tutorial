Implement a Django login and logout system.

### Prerequisites
- Python and Django installed.
- A Django project created (e.g., `myproject`).
- A Django app created (e.g., `myapp`).

### Step-by-Step Guide

#### Step 1: Set Up the Django Project and App
1. **Create a Django project** (if not already done):
   ```bash
   django-admin startproject myproject
   cd myproject
   ```
2. **Create a Django app**:
   ```bash
   python manage.py startapp myapp
   ```
3. **Add the app to `INSTALLED_APPS`** in `myproject/settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'myapp',
       'django.contrib.auth',  # Ensure auth is included
       'django.contrib.contenttypes',  # Required for auth
   ]
   ```
4. **Run migrations** to set up the default database (includes auth tables):
   ```bash
   python manage.py migrate
   ```

#### Step 2: Configure URLs for the Project
1. **Edit `myproject/urls.py`** to include app URLs:
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myapp.urls')),  # Include myapp URLs
   ]
   ```
2. **Create `myapp/urls.py`** to define app-specific URLs:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('login/', views.user_login, name='login'),
       path('logout/', views.user_logout, name='logout'),
       path('dashboard/', views.dashboard, name='dashboard'),
   ]
   ```

#### Step 3: Create Templates
1. **Create a templates directory** in `myapp`:
   ```bash
   mkdir myapp/templates
   ```
2. **Update `myproject/settings.py`** to recognize the templates directory:
   ```python
   TEMPLATES = [
       {
           ...
           'DIRS': [],  # Leave this empty if templates are in app
           ...
       },
   ]
   ```
3. **Create `myapp/templates/base.html`** (base template):
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>{% block title %}My Site{% endblock %}</title>
   </head>
   <body>
       {% if user.is_authenticated %}
           <p>Welcome, {{ user.username }}! <a href="{% url 'logout' %}">Logout</a></p>
       {% else %}
           <p><a href="{% url 'login' %}">Login</a></p>
       {% endif %}
       {% block content %}
       {% endblock %}
   </body>
   </html>
   ```
4. **Create `myapp/templates/login.html`**:
   ```html
   {% extends 'base.html' %}
   {% block title %}Login{% endblock %}
   {% block content %}
       <h2>Login</h2>
       {% if error %}
           <p style="color: red;">{{ error }}</p>
       {% endif %}
       <form method="post">
           {% csrf_token %}
           <p>
               <label for="username">Username:</label>
               <input type="text" name="username" id="username" required>
           </p>
           <p>
               <label for="password">Password:</label>
               <input type="password" name="password" id="password" required>
           </p>
           <button type="submit">Login</button>
       </form>
   {% endblock %}
   ```
5. **Create `myapp/templates/dashboard.html`**:
   ```html
   {% extends 'base.html' %}
   {% block title %}Dashboard{% endblock %}
   {% block content %}
       <h2>Dashboard</h2>
       <p>Welcome, {{ user.username }}! You are logged in.</p>
   {% endblock %}
   ```

#### Step 4: Create Views
1. **Edit `myapp/views.py`** to handle login, logout, and dashboard:
   ```python
   from django.shortcuts import render, redirect
   from django.contrib.auth import authenticate, login, logout
   from django.contrib.auth.decorators import login_required

   def user_login(request):
       if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password']
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('dashboard')
           else:
               return render(request, 'login.html', {'error': 'Invalid username or password'})
       return render(request, 'login.html')

   @login_required
   def dashboard(request):
       return render(request, 'dashboard.html')

   def user_logout(request):
       logout(request)
       return redirect('login')
   ```

#### Step 5: Configure Authentication Settings
1. **Ensure `myproject/settings.py`** has the following (usually default):
   ```python
   AUTHENTICATION_BACKENDS = [
       'django.contrib.auth.backends.ModelBackend',
   ]
   LOGIN_URL = '/login/'  # URL to redirect unauthenticated users
   LOGIN_REDIRECT_URL = '/dashboard/'  # URL after successful login
   LOGOUT_REDIRECT_URL = '/login/'  # URL after logout
   ```

#### Step 6: Create a Superuser for Testing
1. **Create a superuser** to test the login:
   ```bash
   python manage.py createsuperuser
   ```
   - Follow prompts to set username, email, and password.

#### Step 7: Run the Development Server
1. **Start the server**:
   ```bash
   python manage.py runserver
   ```
2. **Access the application**:
   - Open `http://127.0.0.1:8000/login/` in a browser.
   - Log in with the superuser credentials.
   - After login, you should be redirected to the dashboard.
   - Click "Logout" to log out and return to the login page.

#### Step 8: Test the Application
1. **Test login**:
   - Use correct credentials (superuser) to log in.
   - Try incorrect credentials to see the error message.
2. **Test dashboard**:
   - Ensure only authenticated users can access `/dashboard/`.
   - Unauthenticated users should be redirected to `/login/`.
3. **Test logout**:
   - Click logout and confirm redirection to the login page.

#### Step 9: (Optional) Enhance Security
1. **Add CSRF protection** (already included in forms via `{% csrf_token %}`).
2. **Use HTTPS in production** by setting `SECURE_SSL_REDIRECT = True` in `settings.py`.
3. **Limit login attempts** (requires additional packages like `django-axes`).
4. **Password hashing** is handled by Django’s auth system by default.

#### Step 10: (Optional) Use Django’s Built-in Authentication Views
Instead of custom login views, you can use Django’s built-in views for faster setup:
1. **Update `myapp/urls.py`**:
   ```python
   from django.urls import path
   from django.contrib.auth import views as auth_views
   from . import views

   urlpatterns = [
       path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
       path('logout/', auth_views.LogoutView.as_view(), name='logout'),
       path('dashboard/', views.dashboard, name='dashboard'),
   ]
   ```
2. **Ensure `settings.py`** has:
   ```python
   LOGIN_REDIRECT_URL = '/dashboard/'
   LOGOUT_REDIRECT_URL = '/login/'
   ```
3. **Test again** to confirm functionality.

### Notes
- **Templates**: Ensure template paths match exactly (`myapp/templates/`).
- **Static Files**: For CSS/JS, configure `STATIC_URL` and `STATICFILES_DIRS` in `settings.py` and run `python manage.py collectstatic` in production.
- **Production**: Use a proper database (e.g., PostgreSQL) and set `DEBUG = False` in `settings.py`.
- **Error Handling**: Add more robust error messages or logging as needed.
- **User Registration**: This guide covers only login/logout. For registration, add a signup view and form.

This completes the Django login and logout implementation.