# Generated by Django 4.1.7 on 2023-03-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useraccount",
            name="user_type",
            field=models.PositiveSmallIntegerField(choices=[(1, "Driver"), (2, "Cargo Owner")], null=True),
        ),
    ]