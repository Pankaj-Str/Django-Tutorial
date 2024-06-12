from django.urls import path
from p4n_login import views

app_name = "p4n_login"   

urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]