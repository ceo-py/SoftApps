# Generated by Django 4.2.2 on 2023-06-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("discord_bot", "0002_discordbotfeaturesmodel_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="discordbotfeaturesmodel",
            name="data_type",
            field=models.CharField(default="default", max_length=10),
            preserve_default=False,
        ),
    ]
