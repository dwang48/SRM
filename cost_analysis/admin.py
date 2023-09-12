from django.contrib import admin
from .models import ProcessingMethod,Record
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class ProcessingMethodResource(resources.ModelResource):
    class Meta:
        model = ProcessingMethod

@admin.register(ProcessingMethod)
class ProcessingMethodAdmin(ImportExportModelAdmin):
    resource_class = ProcessingMethodResource
    list_display = ('加工方法',)
    search_fields = ('加工方法',)

class RecordResource(resources.ModelResource):
    class Meta:
        model = Record
@admin.register(Record)
class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource
    list_display = ('产品编号', '材料费', '加工费', '运输费','包装费','管理费比例','利润率','总成本')
    search_fields = ('产品编号',)
    # list_filter = ('参与方式',)