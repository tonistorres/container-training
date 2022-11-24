from django.db import models


class User(models.Model):
    nome = models.CharField("nome", max_length=30)
    celular = models.CharField("celular", max_length=15)
    email = models.CharField("email", max_length=30)


def __str__(self):
    return f"Nome: {self.nome}\n Celular: {self.celular}\n Email: {self.email}\n"
