# Generated by Django 4.1 on 2022-12-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="posts",
            name="headline",
            field=models.TextField(
                default="This is the headline",
                help_text="Brief Introduction",
                max_length=400,
            ),
        ),
    ]
