from django.db import models

class Record(models.Model):
    产品编号 = models.CharField(max_length=255)
    材料费 = models.FloatField(null=True, blank=True)
    加工费 = models.FloatField(null=True, blank=True)
    加工明细 = models.CharField(max_length=255, null=True, blank=True)
    运输费 = models.FloatField(null=True, blank=True)
    包装费 = models.FloatField(null=True, blank=True)
    管理费比例 = models.FloatField(null=True, blank=True)
    利润率 = models.FloatField(null=True, blank=True)
    总成本 = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "计算历史"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.产品编号   