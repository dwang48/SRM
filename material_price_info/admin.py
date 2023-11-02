from django.contrib import admin
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin,ExportActionMixin
from .models import *
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


# 公共 Resource 类
class BaseMaterialPriceResource(resources.ModelResource):
    categories = fields.Field(attribute='categories', column_name='类别')
    supplier_name = fields.Field(attribute='supplier_name', column_name='供应商名称')
    supplier_code = fields.Field(attribute='supplier_code', column_name='供应商编码')
    material_name = fields.Field(attribute='material_name', column_name='材料名称')
    material_grade = fields.Field(attribute='material_grade', column_name='材料牌号')
    measurement_unit = fields.Field(attribute='measurement_unit', column_name='计量单位')
    pricing_currency = fields.Field(attribute='pricing_currency', column_name='计价货币')
    price = fields.Field(attribute='price', column_name='价格')
    scrap_price = fields.Field(attribute='scrap_price', column_name='废料价格')
    price_update_date = fields.Field(attribute='price_update_date', column_name='价格更新日期')
    notes = fields.Field(attribute='notes', column_name='备注')
    
    class Meta:
        exclude = ('id',)
        abstract = True
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['material_name',]

# 公共 Admin 类
class BaseMaterialPriceAdmin(ImportExportModelAdmin,ExportActionMixin):
    list_display = ['categories','supplier_name','supplier_code','material_name', 'material_grade', 'measurement_unit', 'pricing_currency', 'price', 'scrap_price', 'price_update_date','notes']
    list_filter = ['supplier_name','supplier_code']
    search_fields = ['supplier_name', 'material_name','supplier_code']


class MaterialPriceResource(BaseMaterialPriceResource):
    class Meta(BaseMaterialPriceResource.Meta):
        model = MaterialPrice

@admin.register(MaterialPrice)
class MaterialPriceAdmin(BaseMaterialPriceAdmin):
    # actions=[export_to_excel]
    resource_class = MaterialPriceResource