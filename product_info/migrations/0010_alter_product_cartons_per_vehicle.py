# Generated by Django 4.2.4 on 2023-10-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_info", "0009_alter_product_options_product_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="cartons_per_vehicle",
            field=models.IntegerField(blank=True, null=True, verbose_name="每车包装量"),
        ),
    ]
