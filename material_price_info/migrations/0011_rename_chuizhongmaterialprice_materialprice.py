# Generated by Django 4.2.4 on 2023-10-11 05:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("material_price_info", "0010_chuizhongmaterialprice_categories"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ChuizhongMaterialPrice",
            new_name="MaterialPrice",
        ),
    ]
