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


class Equipment(models.Model):
    category = models.CharField(max_length=200, verbose_name='采购品类',choices=category_choices)
    supplier_name = models.CharField(max_length=200,verbose_name="供应商名称")
    supplier_code = models.CharField(max_length=200,verbose_name="供应商代码")
    manufacturing_process = models.CharField(max_length=200, verbose_name='制造工艺')
    equipment_name = models.CharField(max_length=200, verbose_name='设备名称')
    equipment_model = models.CharField(max_length=200, verbose_name='设备型号',default='无',null=True)
    current_value = models.FloatField(  verbose_name='设备现价值')
    remaining_depreciation_years = models.IntegerField(verbose_name='剩余折旧年数')
    power_kw = models.FloatField(  verbose_name='设备功率')
    auxiliary_power_a_kw = models.FloatField(  verbose_name='辅助设备A功率',default=0.0,blank=True,null=True)
    auxiliary_power_b_kw = models.FloatField(  verbose_name='辅助设备B功率',default=0.0,blank=True,null=True)
    auxiliary_power_c_kw = models.FloatField(  verbose_name='辅助设备C功率',default=0.0,blank=True,null=True)
    water_consumption = models.FloatField(  verbose_name='耗水量',default=0,blank=True,null=True)
    gas_consumption = models.FloatField(  verbose_name='耗气量',default=0,blank=True,null=True)
    other_resource_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='其他资源名称')
    other_resource_unit = models.CharField(max_length=200, blank=True, null=True, verbose_name='其他资源单位')
    other_resource_consumption = models.FloatField(  verbose_name='其他资源耗用量',default=0,blank=True,null=True)
    other_resource_price = models.FloatField(  verbose_name='其他资源单价',default=0,blank=True,null=True)

    additional_resource_name = models.CharField(max_length=200, blank=True, null = True,verbose_name='附加资源名称')
    additional_resource_unit = models.CharField(max_length=200, blank=True,null=True, verbose_name='附加资源单位',default=0)
    additional_resource_consumption = models.FloatField(  verbose_name='附加资源耗用量',default=0,blank=True,null=True)
    additional_resource_price = models.FloatField(  verbose_name='附加资源单价',default=0,blank=True,null=True)

    additional_resource_name2 = models.CharField(max_length=200, blank=True, null = True,verbose_name='附加资源名称2')
    additional_resource_unit2 = models.CharField(max_length=200, blank=True,null=True, verbose_name='附加资源单位2',default=0)
    additional_resource_consumption2 = models.FloatField(  verbose_name='附加资源耗用量2',default=0,blank=True,null=True)
    additional_resource_price2 = models.FloatField(  verbose_name='附加资源单价2',default=0,blank=True,null=True)

    additional_resource_name3 = models.CharField(max_length=200, blank=True, null = True,verbose_name='附加资源名称3')
    additional_resource_unit3 = models.CharField(max_length=200, blank=True,null=True, verbose_name='附加资源单位3',default=0)
    additional_resource_consumption3 = models.FloatField(  verbose_name='附加资源耗用量3',default=0,blank=True,null=True)
    additional_resource_price3 = models.FloatField(  verbose_name='附加资源单价3',default=0,blank=True,null=True)

    update_date = models.CharField(max_length=200,verbose_name='更新日期',blank=True,null=True)
    notes = models.TextField(null=True, blank=True, verbose_name="备注")
    def __str__(self):
        return self.equipment_name

    class Meta:
        verbose_name = '设备参数'
        verbose_name_plural = '设备参数'
