from django.db import models
from material_price_info.models import MaterialPrice
from vendor_info.models import Vendor
from equipment_info.models import Equipment

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


class Packaging(models.Model):
    quantity = models.IntegerField(null=True, blank=True, verbose_name='标准包装数量')
    size_length = models.FloatField(null=True, blank=True, verbose_name='标准包装尺寸长')
    size_width = models.FloatField(null=True, blank=True, verbose_name='标准包装尺寸宽')
    size_height = models.FloatField(null=True, blank=True, verbose_name='标准包装尺寸高')
    # 可以根据需要添加其他包材相关的字段

class Transportation(models.Model):
    destination = models.CharField(max_length=255, null=True, blank=True, verbose_name='目的地')
    pickup_location = models.CharField(max_length=255, null=True, blank=True, verbose_name='提货地')
    shipping_method = models.CharField(max_length=255, null=True, blank=True, verbose_name='出货方式')
    transport_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='运输方式')
    vehicle_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='运输车型')
    distance = models.FloatField(null=True, blank=True, verbose_name='运输距离')

class Finance(models.Model):
    management_fee = models.FloatField(null=True, blank=True, verbose_name='管理费用')
    profit_margin = models.FloatField(null=True, blank=True, verbose_name='利润率')

class Part(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True, verbose_name='类别',choices=category_choices)
    purchase_part = models.CharField(max_length=255, null=True, blank=True, verbose_name='采购零件')
    part_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='零件编号')
    size_length = models.FloatField(null=True, blank=True, verbose_name='零件尺寸长')
    size_width = models.FloatField(null=True, blank=True, verbose_name='零件尺寸宽')
    size_thickness = models.FloatField(null=True, blank=True, verbose_name='零件尺寸厚度')
    volume = models.FloatField(null=True, blank=True, verbose_name='零件立方')
    manufacturing_process = models.CharField(max_length=255, null=True, blank=True, verbose_name='制造工艺')
    requires_mold = models.BooleanField(null=True, blank=True, verbose_name='需要模具')
    cavities_per_mold = models.IntegerField(null=True, blank=True, verbose_name='穴数/模')
    material_utilization = models.FloatField(null=True, blank=True, verbose_name='材料利用率')
    recycle_usage_rate = models.FloatField(null=True, blank=True, verbose_name='回料使用率')
    production_cycle = models.FloatField(null=True, blank=True, verbose_name='生产周期')
    operator_count = models.IntegerField(null=True, blank=True, verbose_name='操作员数量')
    min_order_quantity = models.IntegerField(null=True, blank=True, verbose_name='最小起订量')
    annual_demand = models.IntegerField(null=True, blank=True, verbose_name='年需求量')
    materials = models.ManyToManyField(MaterialPrice, blank=True, verbose_name='材料')
    supplier = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True, verbose_name='供应商')
    equipments = models.ManyToManyField(Equipment, blank=True, verbose_name='设备')
    packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE, null=True, blank=True, verbose_name='包装')
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE, null=True, blank=True, verbose_name='运输')
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE, null=True, blank=True, verbose_name='财务')
    def save(self, *args, **kwargs):
        # 在保存Part对象之前，确保与category相关联的materials和supplier是正确的
        self.materials = self.materials.filter(categories=self.category)
        if self.supplier and self.category not in self.supplier.categories.all():
            self.supplier = None
        super().save(*args, **kwargs)
