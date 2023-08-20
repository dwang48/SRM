from django.db import models

class Vendor(models.Model):
    supplier_name = models.CharField(max_length=100, verbose_name="供应商")
    supplier_code = models.CharField(max_length=100, verbose_name="供应商代码")
    production_location = models.CharField(max_length=100, verbose_name="生产地点（城市）")
    currency_name = models.CharField(max_length=50, verbose_name="货币名称")
    operator_wages = models.FloatField(verbose_name="操作员工资（元/月）")
    electricity_price = models.FloatField(verbose_name="电价（元/千瓦时）")
    water_price = models.FloatField(verbose_name="水价（元/吨）")
    gas_price = models.FloatField(null=True, blank=True, verbose_name="燃气价（元/立方米）")

    class Meta:
        verbose_name = "供应商信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.supplier_name