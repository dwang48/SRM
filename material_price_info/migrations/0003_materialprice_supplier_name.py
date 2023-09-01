# Generated by Django 4.2.4 on 2023-08-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("material_price_info", "0002_alter_materialprice_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="materialprice",
            name="supplier_name",
            field=models.CharField(default=1, max_length=100, verbose_name="供应商名称"),
            preserve_default=False,
        ),
    ]
