from django.urls import path

from todo_app.views import HomeView


app_name = "todo_app"

urlpatterns = [
    path("", HomeView.as_view(), name="tasks"),
]
