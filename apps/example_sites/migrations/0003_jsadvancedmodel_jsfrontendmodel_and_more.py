# Generated by Django 4.2.2 on 2023-06-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("example_sites", "0002_pythonwebbasicsmodel_site_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="JSAdvancedModel",
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
        migrations.CreateModel(
            name="JSFrontEndModel",
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
        migrations.AddField(
            model_name="pythonwebbasicsmodel",
            name="code_link",
            field=models.URLField(default="default"),
            preserve_default=False,
        ),
    ]
