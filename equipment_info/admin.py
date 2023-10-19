from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
# import csv
# from .models import Equipment

from import_export import resources, fields
from .models import Equipment,Equipment2
import openpyxl

# def export_to_csv(modeladmin, request, queryset):
#     model = modeladmin.model
#     model_name = model._meta.verbose_name_plural  # Get the plural verbose name of the model
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'

#     writer = csv.writer(response)
#     field_names = [field.verbose_name for field in model._meta.fields]

#     writer.writerow(field_names)

#     for obj in queryset:
#         row = [getattr(obj, field.name) for field in model._meta.fields]
#         writer.writerow(row)

#     return response

# export_to_csv.short_description = '导出csv'

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


class EquipmentResource(resources.ModelResource):
    purchase_category = fields.Field(attribute='purchase_category', column_name='采购品类')
    manufacturing_process = fields.Field(attribute='manufacturing_process', column_name='制造工艺')
    equipment_name = fields.Field(attribute='equipment_name', column_name='设备名称')
    equipment_model = fields.Field(attribute='equipment_model', column_name='设备型号')
    current_value = fields.Field(attribute='current_value', column_name='设备现价值')
    remaining_depreciation_years = fields.Field(attribute='remaining_depreciation_years', column_name='剩余折旧年数')
    power_kw = fields.Field(attribute='power_kw', column_name='设备功率（千瓦）')
    lubricating_oil_consumption = fields.Field(attribute='lubricating_oil_consumption', column_name='润滑油消耗耗用量（KG/H)')
    oil_price_per_kg = fields.Field(attribute='oil_price_per_kg', column_name='润滑油消耗单价(元/KG)')
    update_date = fields.Field(attribute='update_date', column_name='更新日期')

    def before_import_row(self, row, **kwargs):
        if not row.get("设备型号"):
            row["设备型号"] = "Unknown"  # or some default value
    class Meta:
        model = Equipment
        # skip_unchanged = True
        # report_skipped = True
        exclude = ('id',)
        import_id_fields = ["purchase_category","manufacturing_process","equipment_name","equipment_model"]
        # fields = ('purchase_category', 'manufacturing_process', 'equipment_name', 'equipment_model', 'current_value', 'remaining_depreciation_years', 'power_kw', 'lubricating_oil_consumption', 'oil_price_per_kg',)

@admin.register(Equipment)
class EquipmentAdmin(ImportExportModelAdmin):
    resource_class = EquipmentResource
    actions = [export_to_excel]
    def formatted_equipment_name(self, obj):
        return f"{obj.equipment_name} (Model: {obj.equipment_model})"
    formatted_equipment_name.admin_order_field = 'equipment_name'  # Allows sorting by this field
    formatted_equipment_name.short_description = 'Equipment'
    list_display = ['purchase_category', 'manufacturing_process', 'equipment_name', 'equipment_model', 'current_value', 'remaining_depreciation_years', 'power_kw', 'lubricating_oil_consumption', 'oil_price_per_kg','update_date']
    list_filter = ['purchase_category', 'manufacturing_process']
    search_fields = ['equipment_name', 'equipment_model']
    



class Equipment2Resource(resources.ModelResource):
    category = fields.Field(attribute='category', column_name='采购品类')
    manufacturing_process = fields.Field(attribute='manufacturing_process', column_name='制造工艺')
    equipment_name = fields.Field(attribute='equipment_name', column_name='设备名称')
    equipment_model = fields.Field(attribute='equipment_model', column_name='设备型号')
    current_value = fields.Field(attribute='current_value', column_name='设备现价值')
    remaining_depreciation_years = fields.Field(attribute='remaining_depreciation_years', column_name='剩余折旧年数')
    power_kw = fields.Field(attribute='power_kw', column_name='设备功率')
    auxiliary_power_a_kw = fields.Field(attribute='auxiliary_power_a_kw', column_name='辅助设备A功率')
    auxiliary_power_b_kw = fields.Field(attribute='auxiliary_power_b_kw', column_name='辅助设备B功率')
    auxiliary_power_c_kw = fields.Field(attribute='auxiliary_power_c_kw', column_name='辅助设备C功率')
    water_consumption = fields.Field(attribute='water_consumption', column_name='耗水量')
    gas_consumption = fields.Field(attribute='gas_consumption', column_name='耗气量')
    other_resource_name = fields.Field(attribute='other_resource_name', column_name='其他资源名称')
    other_resource_unit = fields.Field(attribute='other_resource_unit', column_name='其他资源单位')
    other_resource_consumption = fields.Field(attribute='other_resource_consumption', column_name='其他资源耗用量')
    other_resource_price = fields.Field(attribute='other_resource_price', column_name='其他资源单价')
    additional_resource_name = fields.Field(attribute='additional_resource_name', column_name='附加资源名称')
    additional_resource_unit = fields.Field(attribute='additional_resource_unit', column_name='附加资源单位')
    additional_resource_consumption = fields.Field(attribute='additional_resource_consumption', column_name='附加资源耗用量')
    additional_resource_price = fields.Field(attribute='additional_resource_price', column_name='附加资源单价')
    class Meta:
        model = Equipment2
        # You can include or exclude fields to handle in import/export
        fields = ('category', 'manufacturing_process', 'equipment_name', 'equipment_model',
                  'current_value', 'remaining_depreciation_years', 'power_kw', 'auxiliary_power_a_kw', 'auxiliary_power_b_kw', 'auxiliary_power_c_kw', 
                       'water_consumption', 'gas_consumption', 'other_resource_name', 
                       'other_resource_unit', 'other_resource_consumption', 'other_resource_price',
                       'additional_resource_name', 'additional_resource_unit', 
                       'additional_resource_consumption', 'additional_resource_price'
                  )
        # Optionally, specify fields that you want to exclude from import/export
        # exclude = ('id', )
        # Define any specific import ID fields (useful for import data matching)
        export_order = fields
        import_id_fields = ('category','manufacturing_process','equipment_name', 'equipment_model',)



@admin.register(Equipment2)
class Equipment2Admin(ImportExportModelAdmin):
    resource_class = Equipment2Resource
    actions=[export_to_excel]
    list_display = ('category', 'manufacturing_process', 'equipment_name', 'equipment_model', 
                    'current_value', 'remaining_depreciation_years', 'power_kw','auxiliary_power_a_kw', 'auxiliary_power_b_kw', 'auxiliary_power_c_kw', 
                       'water_consumption', 'gas_consumption', 'other_resource_name', 
                       'other_resource_unit', 'other_resource_consumption', 'other_resource_price',
                       'additional_resource_name', 'additional_resource_unit', 
                       'additional_resource_consumption', 'additional_resource_price')
    search_fields = ('equipment_name', 'equipment_model',)
    list_filter = ('category', 'manufacturing_process',)
