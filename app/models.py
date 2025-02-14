from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

