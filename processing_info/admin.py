from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ProcessingProcedures

class ProcessingProceduresAdmin(admin.ModelAdmin):
    # 设置搜索字段为设备名称和设备型号
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


admin.site.register(ProcessingProcedures, ProcessingProceduresAdmin)

