# Generated by Django 4.2.4 on 2023-08-31 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cost_analysis", "0003_alter_costanalysis_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProcessingMethod",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
    ]
