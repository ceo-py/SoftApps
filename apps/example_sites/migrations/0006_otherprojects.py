# Generated by Django 4.2.2 on 2023-06-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("example_sites", "0005_discordbots_gamesprojects"),
    ]

    operations = [
        migrations.CreateModel(
            name="OtherProjects",
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
                ("image_url", models.URLField()),
                ("site_url", models.URLField()),
                ("code_link", models.URLField()),
            ],
        ),
    ]