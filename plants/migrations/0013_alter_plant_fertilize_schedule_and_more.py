# Generated by Django 4.2.7 on 2024-12-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plants", "0012_plant_fertilize_schedule_plant_repot_schedule_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="fertilize_schedule",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1m", "1 month"),
                    ("2m", "2 months"),
                    ("4m", "4 months"),
                    ("6m", "6 months"),
                    ("1y", "1 year"),
                ],
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="plant",
            name="repot_schedule",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1m", "1 month"),
                    ("2m", "2 months"),
                    ("4m", "4 months"),
                    ("6m", "6 months"),
                    ("1y", "1 year"),
                ],
                max_length=15,
            ),
        ),
    ]
