# Generated by Django 4.2.4 on 2023-10-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cost_analysis", "0010_delete_processingmethod"),
    ]

    operations = [
        migrations.CreateModel(
            name="计算模版",
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
                ("类别", models.CharField(max_length=200, unique=True)),
                ("excel文档", models.FileField(upload_to="计算模版/")),
            ],
        ),
    ]
