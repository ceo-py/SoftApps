# Generated by Django 4.2.2 on 2023-06-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video_lessons", "0002_fundamentalsmidvideolessonsmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="FundamentalsFinalVideoLessonsModel",
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
                ("title", models.CharField()),
                ("video_url", models.CharField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
