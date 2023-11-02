from django.db import models


class Vendor(models.Model):
    category_choices = [
        ("塑料成品", "塑料成品"),
        ("注塑", "注塑"),
        ("喷涂", "喷涂"),
        ("电镀", "电镀"),
        ("烫金", "烫金"),
        ("印刷", "印刷"),
        ("喷绘", "喷绘"),
        ("组装", "组装"),
        ("冲压", "冲压"),
        ("抛光", "抛光"),
        ("氧化", "氧化"),
        ("酸洗", "酸洗"),
        ("刻字", "刻字"),
        ("磁铁", "磁铁"),
        ("垂重", "垂重"),
        ("弹簧", "弹簧"),
        ("铝件成品", "铝件成品"),
        ("栈板", "栈板"),
        ("纸箱/纸板", "纸箱/纸板"),
        ("包装袋", "包装袋"),
        ("彩盒", "彩盒"),
        ("吸塑盘", "吸塑盘"),
        ("转印纸", "转印纸"),
        ("垫片", "垫片"),
        ("箔纸", "箔纸"),
        ("标签", "标签"),
        ("收缩膜", "收缩膜"),
        ("模架", "模架"),
        ("模芯", "模芯"),
        ("玻璃管", "玻璃管"),
        ("棉头", "棉头"),
        ("镜片", "镜片"),
        ("胶头", "胶头"),
        ("刷毛", "刷毛"),
    ]
    categories = models.CharField(
        max_length=100, verbose_name="供应商类别", choices=category_choices
    )
    supplier_name = models.CharField(max_length=100, verbose_name="供应商")
    supplier_code = models.CharField(max_length=100, verbose_name="供应商代码")
    production_location = models.CharField(max_length=100, verbose_name="生产地点（城市）")
    currency_name = models.CharField(max_length=50, verbose_name="货币名称")
    operator_wages = models.FloatField(verbose_name="操作员工资（元/月）")
    electricity_price = models.FloatField(verbose_name="电价（元/千瓦时）")
    water_price = models.FloatField(verbose_name="水价（元/吨）")
    gas_price = models.FloatField(null=True, blank=True, verbose_name="燃气价（元/立方米）")
    update_date = models.CharField(verbose_name="价格更新日期", null=True, blank=True,max_length=200)
    notes = models.TextField(null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "供应商"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.supplier_name
