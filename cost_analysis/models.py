from django.db import models

category_choices = [('塑料成品', '塑料成品'),
    ('注塑', '注塑'),
    ('喷涂', '喷涂'),
    ('电镀', '电镀'),
    ('烫金', '烫金'),
    ('印刷', '印刷'),
    ('喷绘', '喷绘'),
    ('组装', '组装'),
    ('冲压', '冲压'),
    ('抛光', '抛光'),
    ('氧化', '氧化'),
    ('酸洗', '酸洗'),
    ('刻字', '刻字'),
    ('磁铁', '磁铁'),
    ('垂重', '垂重'),
    ('弹簧', '弹簧'),
    ('铝件成品', '铝件成品'),
    ('栈板', '栈板'),
    ('纸箱/纸板', '纸箱/纸板'),
    ('包装袋', '包装袋'),
    ('彩盒', '彩盒'),
    ('吸塑盘', '吸塑盘'),
    ('转印纸', '转印纸'),
    ('垫片', '垫片'),
    ('箔纸', '箔纸'),
    ('标签', '标签'),
    ('收缩膜', '收缩膜'),
    ('模架', '模架'),
    ('模芯', '模芯'),
    ('玻璃管', '玻璃管'),
    ('棉头', '棉头'),
    ('镜片', '镜片'),
    ('胶头', '胶头'),
    ('刷毛', '刷毛')]

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
    
class 计算模版(models.Model):
    类别 = models.CharField(max_length=200, unique=True,choices=category_choices)
    excel文档 = models.FileField(upload_to='计算模版/')
    class Meta:
        verbose_name = "计算模版"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.类别