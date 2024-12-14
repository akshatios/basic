# Generated by Django 5.1.4 on 2024-12-11 04:48

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("news_title", models.CharField(max_length=100)),
                ("news_desc", tinymce.models.HTMLField()),
            ],
        ),
    ]
