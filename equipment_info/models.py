from django.db import models

class Equipment(models.Model):
    purchase_category = models.CharField(max_length=100, verbose_name="采购品类",null=True,blank=True)
    manufacturing_process = models.CharField(max_length=100, verbose_name="制造工艺")
    equipment_name = models.CharField(max_length=255, verbose_name="设备名称", null=True, blank=True)
    equipment_model = models.CharField(max_length=100, verbose_name="设备型号")
    current_value = models.FloatField(max_length=100, verbose_name="设备现价值",null=True,blank=True)
    remaining_depreciation_years = models.IntegerField(verbose_name="剩余折旧年数")
    power_kw = models.FloatField(verbose_name="设备功率（千瓦）")
    lubricating_oil_consumption = models.FloatField(verbose_name="润滑油消耗耗用量（KG/H)")
    oil_price_per_kg = models.FloatField(verbose_name="润滑油消耗单价(元/KG)")
    update_date = models.DateField(verbose_name="价格更新日期",null=True, blank=True)

    class Meta:
        verbose_name = "设备参数(润滑油)"
        verbose_name_plural = "设备参数(润滑油)"


class Equipment2(models.Model):
    category = models.CharField(max_length=200, verbose_name='采购品类')
    manufacturing_process = models.CharField(max_length=200, verbose_name='制造工艺')
    equipment_name = models.CharField(max_length=200, verbose_name='设备名称')
    equipment_model = models.CharField(max_length=200, verbose_name='设备型号')
    current_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='设备现价值')
    remaining_depreciation_years = models.IntegerField(verbose_name='剩余折旧年数')
    power_kw = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='设备功率')
    auxiliary_power_a_kw = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='辅助设备A功率',default=0)
    auxiliary_power_b_kw = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='辅助设备B功率',default=0)
    auxiliary_power_c_kw = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='辅助设备C功率',default=0)
    water_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='耗水量',default=0)
    gas_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='耗气量',default=0)
    other_resource_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='其他资源名称')
    other_resource_unit = models.CharField(max_length=200, blank=True, null=True, verbose_name='其他资源单位')
    other_resource_consumption = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='其他资源耗用量',default=0)
    other_resource_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='其他资源单价',default=0)
    additional_resource_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='附加资源名称')
    additional_resource_unit = models.CharField(max_length=200, blank=True, null=True, verbose_name='附加资源单位')
    additional_resource_consumption = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='附加资源耗用量',default=0)
    additional_resource_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='附加资源单价',default=0)

    def __str__(self):
        return self.equipment_name

    class Meta:
        verbose_name = '设备参数'
        verbose_name_plural = '设备参数'
