from django.contrib import admin
from .models import Record
from import_export import resources
from import_export.admin import ImportExportModelAdmin
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

class RecordResource(resources.ModelResource):
    class Meta:
        model = Record
@admin.register(Record)
class RecordAdmin(ImportExportModelAdmin):
    exclude = ('id',)
    actions=[export_to_excel]
    resource_class = RecordResource
    list_display = ('产品编号', '材料费', '加工费', '加工明细','运输费','包装费','管理费比例','利润率','总成本')
    search_fields = ('产品编号',)
    # list_filter = ('参与方式',)


