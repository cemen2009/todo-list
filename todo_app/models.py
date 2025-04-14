from django.db import models


class TodoTask(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Task: {self.title}"

    class Meta:
        ordering = ['-deadline']
