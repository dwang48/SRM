# Generated by Django 4.2.4 on 2023-10-17 06:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("equipment_info", "0011_equipment2_alter_equipment_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="equipment",
            options={"verbose_name": "设备参数(润滑油)", "verbose_name_plural": "设备参数(润滑油)"},
        ),
    ]
