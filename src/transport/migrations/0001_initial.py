# Generated by Django 4.1.7 on 2023-03-06 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Transport",
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
                ("car_name", models.CharField(max_length=120)),
                ("car_model", models.CharField(max_length=120)),
                ("max_weight", models.PositiveIntegerField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transports",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]