from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    UserName = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    points = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

