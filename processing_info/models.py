from django.db import models

# Create your models here.

class ProcessingProcedures(models.Model):
    equipment_name = models.CharField(max_length=255, verbose_name='设备名称',null=True,blank=True)
    equipment_model = models.CharField(max_length=255, verbose_name='设备型号',null=True,blank=True)
    need_mold = models.CharField(max_length=3, choices=[('Y', '是'), ('N', '否')], verbose_name='需要模具(Y/N)',default='N',null=True,blank=True)
    holes_per_mold = models.IntegerField(verbose_name='穴数/模',null=True,blank=True)
    hourly_capacity = models.IntegerField(verbose_name='每小时产能 （件/小时）',null=True,blank=True)
    operator_count = models.IntegerField(verbose_name='操作员人数',null=True,blank=True)

    class Meta:
        verbose_name = '加工工序'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.equipment_name
    