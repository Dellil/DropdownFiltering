from django.urls import path
from . import views

app_name = "examples"

urlpatterns = [
    path("list", views.ListView.as_view(), name="list"),
    path("all", views.AllView.as_view(), name="all")
]