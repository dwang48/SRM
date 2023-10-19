from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ProcessingProcedures
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin

class ProcessingProceduresResource(resources.ModelResource):
    equipment_name = fields.Field(attribute='equipment_name', column_name='设备名称')
    equipment_model = fields.Field(attribute='equipment_model', column_name='设备型号')
    need_mold = fields.Field(attribute='need_mold', column_name='是否需要模具')
    holes_per_mold = fields.Field(attribute='holes_per_mold', column_name='每模位孔数')
    hourly_capacity = fields.Field(attribute='hourly_capacity', column_name='每小时产能')
    operator_count = fields.Field(attribute='operator_count', column_name='操作工人数')
    class Meta:
        model = ProcessingProcedures
        exclude = ('id',)
        # 设置搜索字段为设备名称和设备型号
        




class ProcessingProceduresAdmin(ImportExportModelAdmin):
    # 设置搜索字段为设备名称和设备型号
    resource_class = ProcessingProceduresResource
    search_fields = ['equipment_name', 'equipment_model']

    # 定义要在列表视图中显示的字段
    list_display = ('equipment_name', 'equipment_model', 'need_mold', 'holes_per_mold', 'hourly_capacity', 'operator_count')

    # 定义可以用于快速筛选的字段
    list_filter = ('need_mold', 'operator_count')

    # 如果你还想添加其他自定义设置，如 list_display, list_filter 等，你可以在这里进行添加
    fieldsets = (
        ('基本信息', {
            'fields': ('equipment_name', 'equipment_model')
        }),
        ('模具和产能', {
            'fields': ('need_mold', 'holes_per_mold', 'hourly_capacity')
        }),
        ('其他信息', {
            'fields': ('operator_count',)
        }),
    )
admin.site.register(ProcessingProcedures,ProcessingProceduresAdmin)
