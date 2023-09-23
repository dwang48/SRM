from django.contrib import admin
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from .models import Vendor

class VendorResource(resources.ModelResource):
    categories = fields.Field(attribute='categories', column_name='类别')
    supplier_name = fields.Field(attribute='supplier_name', column_name='供应商')
    supplier_code = fields.Field(attribute='supplier_code', column_name='供应商代码')
    production_location = fields.Field(attribute='production_location', column_name='生产地点（城市）')
    currency_name = fields.Field(attribute='currency_name', column_name='货币名称')
    operator_wages = fields.Field(attribute='operator_wages', column_name='操作员工资（元/月）')
    electricity_price = fields.Field(attribute='electricity_price', column_name='电价（元/千瓦时）')
    water_price = fields.Field(attribute='water_price', column_name='水价（元/吨）')
    gas_price = fields.Field(attribute='gas_price', column_name='燃气价（元/立方米）')
    update_date = fields.Field(attribute='update_date', column_name='更新日期')
    
    class Meta:
        model = Vendor
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ["supplier_name",]

@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    resource_class = VendorResource
    search_fields = ['categories','supplier_name','supplier_code']
    list_display = ['categories','supplier_name', 'supplier_code', 'production_location', 'currency_name', 'operator_wages', 'electricity_price', 'water_price', 'gas_price','update_date']
