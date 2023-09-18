# Generated by Django 4.2.4 on 2023-09-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessingProcedures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='设备名称')),
                ('equipment_model', models.CharField(blank=True, max_length=255, null=True, verbose_name='设备型号')),
                ('need_mold', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], default='N', max_length=3, null=True, verbose_name='需要模具(Y/N)')),
                ('holes_per_mold', models.IntegerField(blank=True, null=True, verbose_name='穴数/模')),
                ('hourly_capacity', models.IntegerField(blank=True, null=True, verbose_name='每小时产能 （件/小时）')),
                ('operator_count', models.IntegerField(blank=True, null=True, verbose_name='操作员人数')),
            ],
            options={
                'verbose_name': '加工工序',
                'verbose_name_plural': '加工工序',
            },
        ),
    ]
