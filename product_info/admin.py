from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin,ExportActionMixin
from .models import Product
from django.contrib import admin
from django.http import HttpResponse
import openpyxl

def export_to_excel(modeladmin, request, queryset):
    model = modeladmin.model
    model_name = model._meta.verbose_name_plural
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{model_name}.xlsx"'
    
    wb = openpyxl.Workbook()
    ws = wb.active
    field_names = [field.verbose_name for field in model._meta.fields]
    ws.append(field_names)  # Write header
    
    for obj in queryset:
        row = [getattr(obj, field.name) for field in model._meta.fields]
        ws.append(row)  # Write data rows
    
    wb.save(response)
    return response


export_to_excel.short_description = '导出Excel'

class ProductResource(resources.ModelResource):
    categories = fields.Field(attribute='categories', column_name="类别")
    purchase_part = fields.Field(attribute='purchase_part', column_name="采购零件")
    part_number = fields.Field(attribute='part_number', column_name="零件编号")
    part_length = fields.Field(attribute='part_length', column_name="零件尺寸\n长（mm）")
    part_width = fields.Field(attribute='part_width', column_name="零件尺寸\n宽（mm）")
    part_height = fields.Field(attribute='part_height', column_name="零件尺寸\n高（mm）")
    part_gross_weight = fields.Field(attribute='part_gross_weight', column_name="零件毛重\n（克）")
    part_net_weight = fields.Field(attribute='part_net_weight', column_name="零件净重\n（克）")
    material_name = fields.Field(attribute='material_name', column_name="材料名称")
    material_grade = fields.Field(attribute='material_grade', column_name="材料牌号")
    supplier = fields.Field(attribute='supplier', column_name="供应商")
    supplier_code = fields.Field(attribute='supplier_code', column_name="供应商代码")
    equipment_name = fields.Field(attribute='equipment_name', column_name="设备名称")
    equipment_model = fields.Field(attribute='equipment_model', column_name="设备型号")
    need_mold = fields.Field(attribute='need_mold', column_name="需要模具\n（Y/N)")
    holes_per_mold = fields.Field(attribute='holes_per_mold', column_name="穴数/模")
    hourly_capacity = fields.Field(attribute='hourly_capacity', column_name="每小时产能\n（件/小时）")
    operator_count = fields.Field(attribute='operator_count', column_name="操作员人数")
    moq = fields.Field(attribute='moq', column_name="最小起订量\n（MOQ）")
    annual_demand = fields.Field(attribute='annual_demand', column_name="年需求量\n（件/年)")
    standard_packaging_length = fields.Field(attribute='standard_packaging_length', column_name="标准包装尺寸\n长（CM）")
    standard_packaging_width = fields.Field(attribute='standard_packaging_width', column_name="标准包装尺寸\n宽（CM）")
    standard_packaging_height = fields.Field(attribute='standard_packaging_height', column_name="标准包装尺寸\n高（CM）")
    carton_price = fields.Field(attribute='carton_price', column_name="纸箱价格")
    pieces_per_carton = fields.Field(attribute='pieces_per_carton', column_name="每箱包装量\n（件/箱）")
    pe_bag_price = fields.Field(attribute='pe_bag_price', column_name="PE袋价格")
    pieces_per_bag = fields.Field(attribute='pieces_per_bag', column_name="每袋包装量\n（个/袋）")
    transport_type = fields.Field(attribute='transport_type', column_name="运输车型")
    transport_distance = fields.Field(attribute='transport_distance', column_name="运输距离\n（公里）")
    transport_fee_per_vehicle = fields.Field(attribute='transport_fee_per_vehicle', column_name="每车运费")
    cartons_per_vehicle = fields.Field(attribute='cartons_per_vehicle', column_name="每车包装量")
    management_fee_percentage = fields.Field(attribute='management_fee_percentage', column_name="管理费用\n(%)")
    profit_margin_percentage = fields.Field(attribute='profit_margin_percentage', column_name="利润率\n(%)")
    notes = fields.Field(attribute='notes', column_name="备注")

    class Meta:
        model = Product
        # skip_unchanged = True
        # report_skipped = True
        exclude = ('id',)
        import_id_fields = ('part_number',)

# @admin.register(Product)
class ProductAdmin(ImportExportModelAdmin,ExportActionMixin):
    # actions = [export_to_excel]
    resource_class = ProductResource
    list_display = ('categories',
        'purchase_part', 'part_number', 'part_length', 'part_width',
        'part_height', 'part_gross_weight', 'part_net_weight', 'material_name',
        'material_grade', 'supplier', 'supplier_code', 'equipment_name', 'equipment_model',
        'need_mold', 'holes_per_mold', 'hourly_capacity', 'operator_count', 'moq',
        'annual_demand', 'standard_packaging_length', 'standard_packaging_width',
        'standard_packaging_height', 'carton_price', 'pieces_per_carton', 'pe_bag_price',
        'pieces_per_bag', 'transport_type', 'transport_distance', 'transport_fee_per_vehicle',
        'cartons_per_vehicle', 'management_fee_percentage', 'profit_margin_percentage','notes'
    )
    search_fields = ('categories','purchase_part', 'part_number')

admin.site.register(Product,ProductAdmin)