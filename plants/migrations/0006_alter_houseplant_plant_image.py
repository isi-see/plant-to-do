# Generated by Django 4.2.7 on 2024-11-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plants", "0005_houseplant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="houseplant",
            name="plant_image",
            field=models.URLField(blank=True, null=True),
        ),
    ]
