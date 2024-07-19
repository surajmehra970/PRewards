from django.db import models

class TaskData(models.Model):
    TaskName = models.CharField(max_length=50)
    TaskPoints = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
