from django.views import generic

from todo_app.models import TodoTask


class HomeView(generic.ListView):
    template_name = "todo_app/tasks.html"
    queryset = TodoTask.objects.all()
