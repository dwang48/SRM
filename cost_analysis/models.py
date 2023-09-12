from django.db import models




class ProcessingMethod(models.Model):
    加工方法 = models.CharField(max_length=255)

    class Meta:
        verbose_name = "加工方法表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.加工方法

    def calculate(self, *args, **kwargs):
        if self.加工方法 == "剪板":
            # Your shearing_method logic here
            pass
        elif self.加工方法 == "冲压":
            # Your stamping_method logic here
            pass
        # ... and so on for other methods



class Record(models.Model):
    产品编号 = models.CharField(max_length=255)
    材料费 = models.FloatField(null=True, blank=True)
    加工费 = models.FloatField(null=True, blank=True)
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