# Generated by Django 4.2.4 on 2023-10-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("equipment_info", "0029_alter_equipment_update_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="additional_resource_consumption",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="附加资源耗用量"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="additional_resource_consumption2",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="附加资源耗用量2"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="additional_resource_consumption3",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="附加资源耗用量3"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="additional_resource_price",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="附加资源单价"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="additional_resource_price2",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="附加资源单价2"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="additional_resource_price3",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="附加资源单价3"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="auxiliary_power_a_kw",
            field=models.FloatField(
                blank=True, default=0.0, null=True, verbose_name="辅助设备A功率"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="auxiliary_power_b_kw",
            field=models.FloatField(
                blank=True, default=0.0, null=True, verbose_name="辅助设备B功率"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="auxiliary_power_c_kw",
            field=models.FloatField(
                blank=True, default=0.0, null=True, verbose_name="辅助设备C功率"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="current_value",
            field=models.FloatField(verbose_name="设备现价值"),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="gas_consumption",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="耗气量"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="other_resource_consumption",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="其他资源耗用量"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="other_resource_price",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="其他资源单价"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="power_kw",
            field=models.FloatField(verbose_name="设备功率"),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="water_consumption",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="耗水量"
            ),
        ),
    ]