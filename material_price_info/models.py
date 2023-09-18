from django.db import models

# class MaterialPrice(models.Model):
#     supplier_name = models.CharField(max_length=100, verbose_name="供应商名称",blank=True)
#     material_name = models.CharField(max_length=100, verbose_name="材料名称")
#     material_grade = models.CharField(max_length=100, verbose_name="材料牌号")
#     measurement_unit = models.CharField(max_length=50, verbose_name="计量单位")
#     pricing_currency = models.CharField(max_length=50, verbose_name="计价货币")
#     price = models.FloatField(verbose_name="价格")
#     scrap_price = models.FloatField(verbose_name="废料价格")
#     price_update_date = models.DateField(verbose_name="价格更新日期")

#     class Meta:
#         verbose_name = "垂重材料价格"
#         verbose_name_plural = "垂重材料价格"


#     def __str__(self):
#         return self.material_name
    

class BaseMaterialPrice(models.Model):
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
    
class ChuizhongMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "垂重材料价格"
        verbose_name_plural = "垂重材料价格"
    
class SuliaoMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "塑料成品材料价格"
        verbose_name_plural = "塑料成品材料价格"

class ZhusuMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "注塑材料价格"
        verbose_name_plural = "注塑材料价格"

class ShuamaoMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "刷毛材料价格"
        verbose_name_plural = "刷毛材料价格"

class PentuMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "喷涂材料价格"
        verbose_name_plural = "喷涂材料价格"

class DianduMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "电镀材料价格"
        verbose_name_plural = "电镀材料价格"

class TangjinMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "烫金材料价格"
        verbose_name_plural = "烫金材料价格"

class YinshuaMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "印刷材料价格"
        verbose_name_plural = "印刷材料价格"