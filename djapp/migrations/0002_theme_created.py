# Generated by Django 4.2.1 on 2023-06-01 08:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("djapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
