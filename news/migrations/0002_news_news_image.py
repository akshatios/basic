# Generated by Django 5.1.4 on 2024-12-12 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="news_image",
            field=models.FileField(
                default=None, max_length=250, null=True, upload_to="news/"
            ),
        ),
    ]