from django.contrib import admin
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from .models import MaterialPrice

class MaterialPriceResource(resources.ModelResource):
    supplier_name = fields.Field(attribute='supplier_name', column_name='供应商名称')
    material_name = fields.Field(attribute='material_name', column_name='材料名称')
    material_grade = fields.Field(attribute='material_grade', column_name='材料等级')
    measurement_unit = fields.Field(attribute='measurement_unit', column_name='计量单位')
    pricing_currency = fields.Field(attribute='pricing_currency', column_name='计价货币')
    price = fields.Field(attribute='price', column_name='价格')
    scrap_price = fields.Field(attribute='scrap_price', column_name='废料价格')
    price_update_date = fields.Field(attribute='price_update_date', column_name='价格更新日期')
    class Meta:
        model = MaterialPrice
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['material_name',]

@admin.register(MaterialPrice)
class MaterialPriceAdmin(ImportExportModelAdmin):
    resource_class = MaterialPriceResource
    list_display = ['supplier_name','material_name', 'material_grade', 'measurement_unit', 'pricing_currency', 'price', 'scrap_price', 'price_update_date']
    list_filter = ['supplier_name', 'material_name']
    search_fields = ['supplier_name', 'material_name']
