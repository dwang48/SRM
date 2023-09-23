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
        verbose_name = "设备参数"
        verbose_name_plural = "设备参数"


# class Equipment2(models.Model):
#     purchase_category = models.CharField(max_length=100, verbose_name="采购品类",null=True,blank=True)
#     manufacturing_process = models.CharField(max_length=100, verbose_name="制造工艺")
#     equipment_name = models.CharField(max_length=255, verbose_name="设备型号", null=True, blank=True)
#     equipment_model = models.CharField(max_length=100, verbose_name="设备型号")
#     current_value = models.FloatField(max_length=100, verbose_name="设备现价值")
#     remaining_depreciation_years = models.IntegerField(verbose_name="剩余折旧年数")
#     power_kw = models.FloatField(verbose_name="设备功率（千瓦）")
#     lubricating_oil_consumption = models.FloatField(verbose_name="润滑油消耗耗用量（KG/H)")
#     oil_price_per_kg = models.FloatField(verbose_name="润滑油消耗单价(元/KG)")

#     class Meta:
#         verbose_name = "磁铁设备参数"
#         verbose_name_plural = "磁铁设备参数"