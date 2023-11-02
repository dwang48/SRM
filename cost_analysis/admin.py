from django.contrib import admin
from .models import Record,计算模版
from import_export import resources
from import_export.admin import ImportExportModelAdmin,ExportActionMixin
from django.http import HttpResponse
import openpyxl



def export_to_excel(modeladmin, request, queryset):
    model = modeladmin.model
    model_name = model._meta.verbose_name_plural
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{model_name}.xlsx"'
    
    wb = openpyxl.Workbook()
    ws = wb.active
    field_names = [field.verbose_name for field in model._meta.fields if field.name != 'id']  # 排除 'id' 字段
    ws.append(field_names)
    
    for obj in queryset:
        row = [getattr(obj, field.name) for field in model._meta.fields if field.name != 'id']
        ws.append(row)  # Write data rows
    wb.save(response)
    return response


export_to_excel.short_description = '导出Excel'

class RecordResource(resources.ModelResource):
    class Meta:
        model = Record
        exclude = ('id',)
@admin.register(Record)
class RecordAdmin(ImportExportModelAdmin,ExportActionMixin):
    # actions=[export_to_excel]
    resource_class = RecordResource
    list_display = ('产品编号', '材料费', '加工费', '加工明细','运输费','包装费','管理费比例','利润率','总成本')
    search_fields = ('产品编号',)

    def get_actions(self, request):
        actions = super().get_actions(request)
        # if 'export_admin_action' in actions:
        #     del actions['export_admin_action']  # 删除默认的导出操作
        # print("Available actions:", actions)
        return actions


class 计算模版Admin(admin.ModelAdmin):
    list_display = ('类别', 'excel文档',)
    search_fields = ('类别',)

admin.site.register(计算模版, 计算模版Admin)

