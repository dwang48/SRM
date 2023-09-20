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
    
# 垂重
class ChuizhongMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "垂重材料价格"
        verbose_name_plural = "垂重材料价格"
    
#塑料成品
class SuliaoMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "塑料成品材料价格"
        verbose_name_plural = "塑料成品材料价格"

#注塑
class ZhusuMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "注塑材料价格"
        verbose_name_plural = "注塑材料价格"

#刷毛
class ShuamaoMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "刷毛材料价格"
        verbose_name_plural = "刷毛材料价格"

#喷涂
class PentuMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "喷涂材料价格"
        verbose_name_plural = "喷涂材料价格"

#电镀
class DianduMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "电镀材料价格"
        verbose_name_plural = "电镀材料价格"

#烫金
class TangjinMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "烫金材料价格"
        verbose_name_plural = "烫金材料价格"

#印刷
class YinshuaMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "印刷材料价格"
        verbose_name_plural = "印刷材料价格"


#喷绘
class PenhuiMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "喷绘材料价格"
        verbose_name_plural = "喷绘材料价格"

#组装
class ZuzhuangMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "组装材料价格"
        verbose_name_plural = "组装材料价格"

#冲压
class ChongyangMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "冲压材料价格"
        verbose_name_plural = "冲压材料价格"

#切割
class QiegeMaterialPrice(BaseMaterialPrice):
    class Meta(BaseMaterialPrice.Meta):
        verbose_name = "切割材料价格"
        verbose_name_plural = "切割材料价格"

#