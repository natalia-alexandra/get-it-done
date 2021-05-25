from django.db import models


class Todos(models.Model):
    task = models.CharField(max_length=150)

    def __str__(self):
        return self.task
