from django.urls import path
from . import views 

urlpatterns=[
    path("create",views.create),
    path("dashboard",views.dashboard),
    path("edit/<sid>",views.edit),
    path("delete/<did>",views.delete)
]

