# Generated by Django 4.2.4 on 2023-09-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_price_info', '0005_alter_materialprice_supplier_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DianduMaterialPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(blank=True, max_length=100, verbose_name='供应商名称')),
                ('material_name', models.CharField(max_length=100, verbose_name='材料名称')),
                ('material_grade', models.CharField(max_length=100, verbose_name='材料牌号')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='计量单位')),
                ('pricing_currency', models.CharField(max_length=50, verbose_name='计价货币')),
                ('price', models.FloatField(verbose_name='价格')),
                ('scrap_price', models.FloatField(verbose_name='废料价格')),
                ('price_update_date', models.DateField(verbose_name='价格更新日期')),
            ],
            options={
                'verbose_name': '电镀材料价格',
                'verbose_name_plural': '电镀材料价格',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PentuMaterialPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(blank=True, max_length=100, verbose_name='供应商名称')),
                ('material_name', models.CharField(max_length=100, verbose_name='材料名称')),
                ('material_grade', models.CharField(max_length=100, verbose_name='材料牌号')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='计量单位')),
                ('pricing_currency', models.CharField(max_length=50, verbose_name='计价货币')),
                ('price', models.FloatField(verbose_name='价格')),
                ('scrap_price', models.FloatField(verbose_name='废料价格')),
                ('price_update_date', models.DateField(verbose_name='价格更新日期')),
            ],
            options={
                'verbose_name': '喷涂材料价格',
                'verbose_name_plural': '喷涂材料价格',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShuamaoMaterialPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(blank=True, max_length=100, verbose_name='供应商名称')),
                ('material_name', models.CharField(max_length=100, verbose_name='材料名称')),
                ('material_grade', models.CharField(max_length=100, verbose_name='材料牌号')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='计量单位')),
                ('pricing_currency', models.CharField(max_length=50, verbose_name='计价货币')),
                ('price', models.FloatField(verbose_name='价格')),
                ('scrap_price', models.FloatField(verbose_name='废料价格')),
                ('price_update_date', models.DateField(verbose_name='价格更新日期')),
            ],
            options={
                'verbose_name': '刷毛材料价格',
                'verbose_name_plural': '刷毛材料价格',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuliaoMaterialPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(blank=True, max_length=100, verbose_name='供应商名称')),
                ('material_name', models.CharField(max_length=100, verbose_name='材料名称')),
                ('material_grade', models.CharField(max_length=100, verbose_name='材料牌号')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='计量单位')),
                ('pricing_currency', models.CharField(max_length=50, verbose_name='计价货币')),
                ('price', models.FloatField(verbose_name='价格')),
                ('scrap_price', models.FloatField(verbose_name='废料价格')),
                ('price_update_date', models.DateField(verbose_name='价格更新日期')),
            ],
            options={
                'verbose_name': '塑料成品材料价格',
                'verbose_name_plural': '塑料成品材料价格',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TangjinMaterialPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(blank=True, max_length=100, verbose_name='供应商名称')),
                ('material_name', models.CharField(max_length=100, verbose_name='材料名称')),
                ('material_grade', models.CharField(max_length=100, verbose_name='材料牌号')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='计量单位')),
                ('pricing_currency', models.CharField(max_length=50, verbose_name='计价货币')),
                ('price', models.FloatField(verbose_name='价格')),
                ('scrap_price', models.FloatField(verbose_name='废料价格')),
                ('price_update_date', models.DateField(verbose_name='价格更新日期')),
            ],
            options={
                'verbose_name': '烫金材料价格',
                'verbose_name_plural': '烫金材料价格',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YinshuaMaterialPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(blank=True, max_length=100, verbose_name='供应商名称')),
                ('material_name', models.CharField(max_length=100, verbose_name='材料名称')),
                ('material_grade', models.CharField(max_length=100, verbose_name='材料牌号')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='计量单位')),
                ('pricing_currency', models.CharField(max_length=50, verbose_name='计价货币')),
                ('price', models.FloatField(verbose_name='价格')),
                ('scrap_price', models.FloatField(verbose_name='废料价格')),
                ('price_update_date', models.DateField(verbose_name='价格更新日期')),
            ],
            options={
                'verbose_name': '印刷材料价格',
                'verbose_name_plural': '印刷材料价格',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ZhusuMaterialPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(blank=True, max_length=100, verbose_name='供应商名称')),
                ('material_name', models.CharField(max_length=100, verbose_name='材料名称')),
                ('material_grade', models.CharField(max_length=100, verbose_name='材料牌号')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='计量单位')),
                ('pricing_currency', models.CharField(max_length=50, verbose_name='计价货币')),
                ('price', models.FloatField(verbose_name='价格')),
                ('scrap_price', models.FloatField(verbose_name='废料价格')),
                ('price_update_date', models.DateField(verbose_name='价格更新日期')),
            ],
            options={
                'verbose_name': '注塑材料价格',
                'verbose_name_plural': '注塑材料价格',
                'abstract': False,
            },
        ),
    ]
