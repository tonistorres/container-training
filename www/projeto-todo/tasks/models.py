from django.db import models


class Task(models.Model):
    STATUS = (("doing", "Doing"), ("done", "Done"))
    title = models.CharField("title", max_length=100)
    resumetask = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )

    def __str__(self):
        return self.title
