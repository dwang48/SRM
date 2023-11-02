from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin,ExportActionMixin
from django.http import HttpResponse
# import csv
# from .models import Equipment

from import_export import resources, fields
from .models import Equipment
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
    



class EquipmentResource(resources.ModelResource):
    category = fields.Field(attribute='category', column_name='采购品类')
    supplier_name = fields.Field(attribute='supplier_name', column_name='供应商名称')
    supplier_code = fields.Field(attribute='supplier_code', column_name='供应商代码')
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

    additional_resource_name2 = fields.Field(attribute='addtional_resource_name2', column_name='附加资源名称2')
    additional_resource_unit2 = fields.Field(attribute='addtional_resource_unit2', column_name='附加资源单位2')
    additional_resource_consumption2 = fields.Field(attribute='addtional_resource_consumption2', column_name='附加资源耗用量2')
    additional_resource_price2 = fields.Field(attribute='addtional_resource_price2', column_name='附加资源单价2')

    additional_resource_name3 = fields.Field(attribute='additional_resource_name3', column_name='附加资源名称3')
    additional_resource_unit3 = fields.Field(attribute='additional_resource_unit3', column_name='附加资源单位3')
    additional_resource_consumption3 = fields.Field(attribute='additional_resource_consumption3', column_name='附加资源耗用量3')
    additional_resource_price3 = fields.Field(attribute='additional_resource_price3', column_name='附加资源单价3')


    update_date = fields.Field(attribute='update_date', column_name='更新日期')
    notes = fields.Field(attribute='notes', column_name='备注')
    def clean(self, obj):
        for field in Equipment._meta.fields:
            if field.null and getattr(obj, field.name, None) == "":
                setattr(obj, field.name, 0)
        super().clean(obj)
    def before_import_row(self, row, **kwargs):
        for field_name, field_obj in self.fields.items():
            if not row.get(field_obj.column_name) or row[field_obj.column_name] == '':
                row[field_obj.column_name] = 0

    def save(self, *args, **kwargs):
        if self.equipment_model == "":
            self.equipment_model = "无"
        super(Equipment, self).save(*args, **kwargs)
    class Meta:
        model = Equipment
        # You can include or exclude fields to handle in import/export
        fields = ('category', 'supplier_name','supplier_code','manufacturing_process', 'equipment_name', 'equipment_model',
                  'current_value', 'remaining_depreciation_years', 'power_kw', 'auxiliary_power_a_kw', 'auxiliary_power_b_kw', 'auxiliary_power_c_kw', 
                       'water_consumption', 'gas_consumption', 'other_resource_name', 
                       'other_resource_unit', 'other_resource_consumption', 'other_resource_price',
                       'additional_resource_name', 'additional_resource_unit', 
                       'additional_resource_consumption', 'additional_resource_price',
                       #add all the above additional fields:
                       'additional_resource_name2','additional_resource_unit2', 'additional_resource_consumption2', 'additional_resource_price2',
                       'additional_resource_name3','additional_resource_unit3', 'additional_resource_consumption3', 'additional_resource_price3',
                       'update_date','notes',
                  )
        # Optionally, specify fields that you want to exclude from import/export
        exclude = ('id', )
        # Define any specific import ID fields (useful for import data matching)
        export_order = fields
        import_id_fields = ('category','manufacturing_process','equipment_name', 'equipment_model',)



@admin.register(Equipment)
class EquipmentAdmin(ImportExportModelAdmin,ExportActionMixin):
    resource_class = EquipmentResource
    # actions=[export_to_excel]
    list_display = ('category', 'supplier_name','supplier_code','manufacturing_process', 'equipment_name', 'equipment_model', 
                    'current_value', 'remaining_depreciation_years', 'power_kw','auxiliary_power_a_kw', 'auxiliary_power_b_kw', 'auxiliary_power_c_kw', 
                       'water_consumption', 'gas_consumption', 'other_resource_name', 
                       'other_resource_unit', 'other_resource_consumption', 'other_resource_price',
                       'additional_resource_name', 'additional_resource_unit', 
                       'additional_resource_consumption', 'additional_resource_price',
                       #add all the above additional fields:
                       'additional_resource_name2','additional_resource_unit2', 'additional_resource_consumption2', 'additional_resource_price2',
                       'additional_resource_name3','additional_resource_unit3', 'additional_resource_consumption3', 'additional_resource_price3',
                       'update_date','notes')
    search_fields = ('supplier_name','supplier_code','equipment_name', 'equipment_model',)
    list_filter = ('category', 'manufacturing_process',)
