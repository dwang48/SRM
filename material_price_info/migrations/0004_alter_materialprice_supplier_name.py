# Generated by Django 4.2.4 on 2023-08-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("material_price_info", "0003_materialprice_supplier_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="materialprice",
            name="supplier_name",
            field=models.CharField(max_length=100, null=True, verbose_name="供应商名称"),
        ),
    ]
