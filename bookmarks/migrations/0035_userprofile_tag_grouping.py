# Generated by Django 5.0.3 on 2024-05-14 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0034_bookmark_preview_image_file_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="tag_grouping",
            field=models.CharField(
                choices=[("alphabetical", "Alphabetical"), ("disabled", "Disabled")],
                default="alphabetical",
                max_length=12,
            ),
        ),
    ]