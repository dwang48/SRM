from django.contrib import admin
from .models import CostAnalysis
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CostAnalysisResource(resources.ModelResource):
    class Meta:
        model = CostAnalysis

@admin.register(CostAnalysis)
class CostAnalysisAdmin(ImportExportModelAdmin):
    resource_class = CostAnalysisResource
    list_display = ('产品描述', '公式', '参与方式')
    search_fields = ('产品描述',)
    list_filter = ('参与方式',)
