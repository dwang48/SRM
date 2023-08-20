# Generated by Django 4.2.4 on 2023-08-16 22:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Equipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "purchase_category",
                    models.CharField(max_length=100, verbose_name="采购品类"),
                ),
                (
                    "manufacturing_process",
                    models.CharField(max_length=100, verbose_name="制造工艺"),
                ),
                (
                    "equipment_name",
                    models.CharField(max_length=100, verbose_name="设备名称"),
                ),
                (
                    "equipment_model",
                    models.CharField(max_length=100, verbose_name="设备型号"),
                ),
                (
                    "current_value",
                    models.CharField(max_length=100, verbose_name="设备现价值"),
                ),
                (
                    "remaining_depreciation_years",
                    models.IntegerField(verbose_name="剩余折旧年数"),
                ),
                ("power_kw", models.FloatField(verbose_name="设备功率（千瓦）")),
                (
                    "lubricating_oil_consumption",
                    models.FloatField(verbose_name="润滑油消耗耗用量（KG/H)"),
                ),
                ("oil_price_per_kg", models.FloatField(verbose_name="润滑油消耗单价(元/KG)")),
            ],
        ),
    ]