from django.db import models

class CostAnalysis(models.Model):
    产品描述 = models.TextField(null=True, blank=True)
    公式 = models.TextField(null=True, blank=True)
    参与方式 = models.TextField(null=True, blank=True)

    # excel_file = models.FileField(upload_to='cost_analysis_files/')

    class Meta:
        verbose_name = "垂重成本计算"
        verbose_name_plural = "垂重成本计算"

    def __str__(self):
        return self.产品描述

