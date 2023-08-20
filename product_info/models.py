from django.db import models

class Product(models.Model):
    part_name = models.CharField(max_length=100, verbose_name="采购零件")
    part_number = models.CharField(max_length=100, verbose_name="零件编号")
    length = models.FloatField(null=True, blank=True, verbose_name="零件尺寸长（mm）")
    width = models.FloatField(null=True, blank=True, verbose_name="零件尺寸宽（mm）")
    height = models.FloatField(null=True, blank=True, verbose_name="零件尺寸高（mm）")
    gross_weight = models.FloatField(null=True, blank=True, verbose_name="零件毛重（克）")
    net_weight = models.FloatField(null=True, blank=True, verbose_name="零件净重（克）")
    material_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="材料名称")
    material_grade = models.CharField(max_length=100, null=True, blank=True, verbose_name="材料牌号")
    supplier = models.CharField(max_length=100, null=True, blank=True, verbose_name="供应商")
    # ... [Add fields for the remaining columns with their corresponding verbose_name in Chinese]

    class Meta:
        verbose_name = "产品信息"
        verbose_name_plural = "产品信息"

