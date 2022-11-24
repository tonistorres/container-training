from django.db import models


class User(models.Model):
    tarefa = models.CharField("tarefa", max_length=50)


def __str__(self):
    return f"Tarefa: {self.tarefa}\n"
