from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=255)  # Ensure this field is defined
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
