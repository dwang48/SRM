from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Equipment

from import_export import resources, fields
from .models import Equipment,Equipment2

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

    def before_import_row(self, row, **kwargs):
        if not row.get("设备型号"):
            row["设备型号"] = "Unknown"  # or some default value
    class Meta:
        model = Equipment
        # skip_unchanged = True
        # report_skipped = True
        # exclude = ('id',)
        import_id_fields = ["purchase_category","manufacturing_process","equipment_name","equipment_model"]
        # fields = ('purchase_category', 'manufacturing_process', 'equipment_name', 'equipment_model', 'current_value', 'remaining_depreciation_years', 'power_kw', 'lubricating_oil_consumption', 'oil_price_per_kg',)

@admin.register(Equipment)
class EquipmentAdmin(ImportExportModelAdmin):
    resource_class = EquipmentResource
    def formatted_equipment_name(self, obj):
        return f"{obj.equipment_name} (Model: {obj.equipment_model})"
    formatted_equipment_name.admin_order_field = 'equipment_name'  # Allows sorting by this field
    formatted_equipment_name.short_description = 'Equipment'
    list_display = ['purchase_category', 'manufacturing_process', 'equipment_name', 'equipment_model', 'current_value', 'remaining_depreciation_years', 'power_kw', 'lubricating_oil_consumption', 'oil_price_per_kg',]
    list_filter = ['purchase_category', 'manufacturing_process']
    search_fields = ['equipment_name', 'equipment_model']
    # def get_instance(self, instance_loader, row):
    #     return False


class EquipmentResource2(resources.ModelResource):
    purchase_category = fields.Field(attribute='purchase_category', column_name='采购品类')
    manufacturing_process = fields.Field(attribute='manufacturing_process', column_name='制造工艺')
    equipment_name = fields.Field(attribute='equipment_name', column_name='设备名称')
    equipment_model = fields.Field(attribute='equipment_model', column_name='设备型号')
    current_value = fields.Field(attribute='current_value', column_name='设备现价值')
    remaining_depreciation_years = fields.Field(attribute='remaining_depreciation_years', column_name='剩余折旧年数')
    power_kw = fields.Field(attribute='power_kw', column_name='设备功率（千瓦）')
    lubricating_oil_consumption = fields.Field(attribute='lubricating_oil_consumption', column_name='润滑油消耗耗用量（KG/H)')
    oil_price_per_kg = fields.Field(attribute='oil_price_per_kg', column_name='润滑油消耗单价(元/KG)')

    def before_import_row(self, row, **kwargs):
        if not row.get("设备型号"):
            row["设备型号"] = "Unknown"  # or some default value
    class Meta:
        model = Equipment2
        import_id_fields = ["purchase_category",]

@admin.register(Equipment2)
class EquipmentAdmin2(ImportExportModelAdmin):
    resource_class = EquipmentResource
    list_display = ['purchase_category', 'manufacturing_process', 'equipment_name', 'equipment_model', 'current_value', 'remaining_depreciation_years', 'power_kw', 'lubricating_oil_consumption', 'oil_price_per_kg',]
    # def get_instance(self, instance_loader, row):
    #     return False