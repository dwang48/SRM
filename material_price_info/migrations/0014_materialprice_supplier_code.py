# Generated by Django 4.2.4 on 2023-10-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("material_price_info", "0013_alter_materialprice_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="materialprice",
            name="supplier_code",
            field=models.CharField(blank=True, max_length=100, verbose_name="供应商代码"),
        ),
    ]
