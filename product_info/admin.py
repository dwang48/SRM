from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from .models import Product
from django.contrib import admin

class ProductResource(resources.ModelResource):
    part_name = fields.Field(attribute='part_name',column_name="采购零件")
    part_number = fields.Field(attribute='part_number',column_name="零件号")
    length = fields.Field(attribute='length',column_name="零件尺寸长（mm）")
    width = fields.Field(attribute='width',column_name="零件尺寸宽（mm）")
    height = fields.Field(attribute='height',column_name="零件尺寸高（mm）")
    # part_quantity = fields.Field(attribute='part_quantity',column_name="采购数量")
    gross_weight = fields.Field(attribute='gross_weight',column_name="零件毛重（克）")
    net_weight = fields.Field(attribute='net_weight',column_name="零件净重（克）")
    material_name = fields.Field(attribute='material_name',column_name="材料名称")
    material_grade = fields.Field(attribute='material_grade',column_name="材料牌号")
    supplier = fields.Field(attribute='supplier',column_name="供应商")

    class Meta:
        model = Product
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('part_number',)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ['part_name', 'part_number', 'length', 'width', 'height', 'gross_weight', 'net_weight', 'material_name', 'material_grade', 'supplier']
