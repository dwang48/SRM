from django.db import models

class MaterialPrice(models.Model):
    material_name = models.CharField(max_length=100, verbose_name="材料名称")
    material_grade = models.CharField(max_length=100, verbose_name="材料牌号")
    measurement_unit = models.CharField(max_length=50, verbose_name="计量单位")
    pricing_currency = models.CharField(max_length=50, verbose_name="计价货币")
    price = models.FloatField(verbose_name="价格")
    scrap_price = models.FloatField(verbose_name="废料价格")
    price_update_date = models.DateField(verbose_name="价格更新日期")

    class Meta:
        verbose_name = "垂重材料价格"
        verbose_name_plural = "垂重材料价格"

    def __str__(self):
        return self.material_name