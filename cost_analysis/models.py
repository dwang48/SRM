from django.db import models

from django.db import models

class CostAnalysis(models.Model):
    产品描述 = models.TextField(null=True, blank=True)
    公式 = models.TextField(null=True, blank=True)
    参与方式 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "成本计算"
        verbose_name_plural = "成本计算"

    def __str__(self):
        return self.产品描述

