# Generated by Django 4.1 on 2022-12-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0006_posts_full_story_alter_posts_date_posted_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="date_posted",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
