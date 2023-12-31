# Generated by Django 4.2.4 on 2023-11-04 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_info', '0030_alter_equipment_additional_resource_consumption_and_more'),
        ('vendor_info', '0008_alter_vendor_update_date'),
        ('product', '0002_delete_material_alter_part_materials'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.AlterField(
            model_name='part',
            name='equipments',
            field=models.ManyToManyField(blank=True, to='equipment_info.equipment', verbose_name='设备'),
        ),
        migrations.AlterField(
            model_name='part',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_info.vendor', verbose_name='供应商'),
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
