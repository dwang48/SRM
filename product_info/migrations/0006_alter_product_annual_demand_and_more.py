# Generated by Django 4.2.4 on 2023-08-29 07:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_info", "0005_alter_product_annual_demand_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="annual_demand",
            field=models.IntegerField(
                blank=True,
                default=-1,
                null=True,
                verbose_name="年需求量 （件/年,null=True,blank=True)",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="carton_price",
            field=models.FloatField(
                blank=True, default=-1, null=True, verbose_name="纸箱价格"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="cartons_per_vehicle",
            field=models.IntegerField(
                blank=True, default=-1, null=True, verbose_name="每车箱数"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="equipment_model",
            field=models.CharField(
                blank=True,
                default="未定义",
                max_length=255,
                null=True,
                verbose_name="设备型号",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="equipment_name",
            field=models.CharField(
                blank=True,
                default="未定义",
                max_length=255,
                null=True,
                verbose_name="设备名称",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="holes_per_mold",
            field=models.IntegerField(
                blank=True, default=-1, null=True, verbose_name="穴数/模"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="hourly_capacity",
            field=models.IntegerField(
                blank=True, default=-1, null=True, verbose_name="每小时产能 （件/小时）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="management_fee_percentage",
            field=models.FloatField(
                blank=True,
                default=0,
                null=True,
                verbose_name="管理费用 (%,null=True,blank=True)",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="material_grade",
            field=models.CharField(
                blank=True,
                default="未命名",
                max_length=255,
                null=True,
                verbose_name="材料牌号",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="material_name",
            field=models.CharField(
                blank=True,
                default="未命名",
                max_length=255,
                null=True,
                verbose_name="材料名称",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="moq",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="最小起订量 （MOQ）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="need_mold",
            field=models.CharField(
                blank=True,
                choices=[("Y", "是"), ("N", "否")],
                default="N",
                max_length=3,
                null=True,
                verbose_name="需要模具(Y/N)",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="operator_count",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="操作员人数"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="part_gross_weight",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="零件毛重 （克）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="part_height",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="零件尺寸 高（mm）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="part_length",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="零件尺寸 长（mm）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="part_net_weight",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="零件净重 （克）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="part_number",
            field=models.CharField(
                blank=True,
                default="未命名",
                max_length=255,
                null=True,
                verbose_name="零件编号",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="part_width",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="零件尺寸 宽（mm）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="pe_bag_price",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="PE袋价格"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="pieces_per_bag",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="每袋包装量 （个/袋）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="pieces_per_carton",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="每箱包装量 （件/箱）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="profit_margin_percentage",
            field=models.FloatField(
                blank=True,
                default=0,
                null=True,
                verbose_name="利润率 (%,null=True,blank=True)",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="purchase_part",
            field=models.CharField(
                blank=True,
                default="未命名",
                max_length=255,
                null=True,
                verbose_name="采购零件",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="standard_packaging_height",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="标准包装尺寸 高（CM）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="standard_packaging_length",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="标准包装尺寸 长（CM）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="standard_packaging_width",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="标准包装尺寸 宽（CM）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="supplier",
            field=models.CharField(
                blank=True, default="未命名", max_length=255, null=True, verbose_name="供应商"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="supplier_code",
            field=models.CharField(
                blank=True,
                default="未命名",
                max_length=255,
                null=True,
                verbose_name="供应商代码",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="transport_distance",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="运输距离 （公里）"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="transport_fee_per_vehicle",
            field=models.FloatField(
                blank=True, default=0, null=True, verbose_name="每车运费"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="transport_type",
            field=models.CharField(
                blank=True,
                default="未命名",
                max_length=255,
                null=True,
                verbose_name="运输车型",
            ),
        ),
    ]
