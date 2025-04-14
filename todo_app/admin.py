from django.contrib import admin

from todo_app.models import TodoTask


@admin.register(TodoTask)
class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "deadline", "is_completed")
    list_filter = ("is_completed",)
    search_fields = ("title",)
    ordering = ("-deadline", "-created_at")
