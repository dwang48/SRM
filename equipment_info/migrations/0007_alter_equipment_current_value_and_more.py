# Generated by Django 4.2.4 on 2023-09-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_info', '0006_alter_equipment_equipment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='current_value',
            field=models.FloatField(max_length=100, verbose_name='设备现价值'),
        ),
        migrations.AlterField(
            model_name='equipment2',
            name='current_value',
            field=models.FloatField(max_length=100, verbose_name='设备现价值'),
        ),
    ]