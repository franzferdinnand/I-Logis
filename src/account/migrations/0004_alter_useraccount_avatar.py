# Generated by Django 3.2.16 on 2023-09-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_useraccount_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(upload_to='media/avatars'),
        ),
    ]