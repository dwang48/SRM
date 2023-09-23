from django.db import models    

class BaseMaterialPrice(models.Model):
    categories = models.CharField(max_length=100, verbose_name="类别")
    supplier_name = models.CharField(max_length=100, verbose_name="供应商名称", blank=True)
    material_name = models.CharField(max_length=100, verbose_name="材料名称")
    material_grade = models.CharField(max_length=100, verbose_name="材料牌号")
    measurement_unit = models.CharField(max_length=50, verbose_name="计量单位")
    pricing_currency = models.CharField(max_length=50, verbose_name="计价货币")
    price = models.FloatField(verbose_name="价格")
    scrap_price = models.FloatField(verbose_name="废料价格")
    price_update_date = models.DateField(verbose_name="价格更新日期")

    class Meta:
        abstract = True

    def __str__(self):
        return self.material_name
    
# 垂重
class ChuizhongMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "材料价格"
        verbose_name_plural = "材料价格"

#