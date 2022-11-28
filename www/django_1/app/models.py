from django.db import models


class User(models.Model):
    nome = models.CharField("nome", max_length=60)
    celular = models.BigIntegerField("celular")
