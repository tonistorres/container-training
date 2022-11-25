# Generated by Django 4.1.3 on 2022-11-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30, verbose_name="nome")),
                ("celular", models.CharField(max_length=15, verbose_name="celular")),
                ("email", models.CharField(max_length=30, verbose_name="email")),
            ],
        ),
    ]