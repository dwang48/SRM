from django.db import models

class Product(models.Model):
    purchase_part = models.CharField(max_length=255, verbose_name='采购零件',null=True,blank=True)
    part_number = models.CharField(max_length=255, verbose_name='零件编号',null=True,blank=True)
    part_length = models.FloatField(verbose_name='零件尺寸 长（mm）',null=True,blank=True)
    part_width = models.FloatField(verbose_name='零件尺寸 宽（mm）',null=True,blank=True)
    part_height = models.FloatField(verbose_name='零件尺寸 高（mm）',null=True,blank=True)
    part_gross_weight = models.FloatField(verbose_name='零件毛重 （克）',null=True,blank=True)
    part_net_weight = models.FloatField(verbose_name='零件净重 （克）',null=True,blank=True)
    material_name = models.CharField(max_length=255, verbose_name='材料名称',null=True,blank=True)
    material_grade = models.CharField(max_length=255, verbose_name='材料牌号',null=True,blank=True)
    supplier = models.CharField(max_length=255, verbose_name='供应商',null=True,blank=True)
    supplier_code = models.CharField(max_length=255, verbose_name='供应商代码',null=True,blank=True)
    equipment_name = models.CharField(max_length=255, verbose_name='设备名称',null=True,blank=True)
    equipment_model = models.CharField(max_length=255, verbose_name='设备型号',null=True,blank=True)
    need_mold = models.CharField(max_length=3, choices=[('Y', '是'), ('N', '否')], verbose_name='需要模具(Y/N)',default='N',null=True,blank=True)
    holes_per_mold = models.IntegerField(verbose_name='穴数/模',null=True,blank=True)
    hourly_capacity = models.IntegerField(verbose_name='每小时产能 （件/小时）',null=True,blank=True)
    operator_count = models.IntegerField(verbose_name='操作员人数',null=True,blank=True)
    moq = models.IntegerField(verbose_name='最小起订量 （MOQ）',null=True,blank=True)
    annual_demand = models.IntegerField(verbose_name='年需求量 （件/年)',null=True,blank=True)
    standard_packaging_length = models.FloatField(verbose_name='标准包装尺寸 长（CM）',null=True,blank=True)
    standard_packaging_width = models.FloatField(verbose_name='标准包装尺寸 宽（CM）',null=True,blank=True)
    standard_packaging_height = models.FloatField(verbose_name='标准包装尺寸 高（CM）',null=True,blank=True)
    carton_price = models.FloatField(verbose_name='纸箱价格',null=True,blank=True)
    pieces_per_carton = models.IntegerField(verbose_name='每箱包装量 （件/箱）',null=True,blank=True)
    pe_bag_price = models.FloatField(verbose_name='PE袋价格',null=True,blank=True)
    pieces_per_bag = models.IntegerField(verbose_name='每袋包装量 （个/袋）',null=True,blank=True)
    transport_type = models.CharField(max_length=255, verbose_name='运输车型',null=True,blank=True)
    transport_distance = models.FloatField(verbose_name='运输距离 （公里）',null=True,blank=True)
    transport_fee_per_vehicle = models.FloatField(verbose_name='每车运费',null=True,blank=True)
    cartons_per_vehicle = models.IntegerField(verbose_name='每车箱数',null=True,blank=True)
    management_fee_percentage = models.FloatField(verbose_name='管理费用 (%)',null=True,blank=True)
    profit_margin_percentage = models.FloatField(verbose_name='利润率 (%)',null=True,blank=True)

    # def __str__(self,null=True,blank=True):
    #     return self.purchase_part
    def __str__(self):
        return str(self.purchase_part) if self.purchase_part else ''

    class Meta:
        verbose_name = "垂重产品信息"
        verbose_name_plural = "垂重产品信息"

