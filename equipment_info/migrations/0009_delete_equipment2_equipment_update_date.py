# Generated by Django 4.2.4 on 2023-09-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("equipment_info", "0008_alter_equipment_current_value"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Equipment2",
        ),
        migrations.AddField(
            model_name="equipment",
            name="update_date",
            field=models.DateField(blank=True, null=True, verbose_name="价格更新日期"),
        ),
    ]
