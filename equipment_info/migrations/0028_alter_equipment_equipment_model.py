# Generated by Django 4.2.4 on 2023-10-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("equipment_info", "0027_alter_equipment_equipment_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="equipment_model",
            field=models.CharField(
                default="无", max_length=200, null=True, verbose_name="设备型号"
            ),
        ),
    ]
