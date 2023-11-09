from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .models import Packaging, Transportation, Finance, Part
from vendor_info.models import Vendor
from equipment_info.models import Equipment
from material_price_info.models import MaterialPrice

class PartResource(resources.ModelResource):
    materials = fields.Field(attribute='materials', column_name="材料")
    supplier_name = fields.Field(attribute='supplier__name', column_name="供应商")
    supplier_code = fields.Field(attribute='supplier__code', column_name="供应商代码")
    equipments = fields.Field(attribute='equipments', column_name="设备")
    packaging_quantity = fields.Field(attribute='packaging__quantity', column_name="标准包装数量")
    transportation_destination = fields.Field(attribute='transportation__destination', column_name="目的地")
    finance_management_fee = fields.Field(attribute='finance__management_fee', column_name="管理费用")

    def dehydrate_materials(self, part):
        return ', '.join([material.name for material in part.materials.all()])

    class Meta:
        model = Part
        exclude = ('id',)
        fields= '__all__'
        import_id_fields = ('part_number',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        # if instance:
        #     # 根据 Part 的 category 来过滤 Vendor 和 MaterialPrice
        #     self.fields['supplier'].queryset = Vendor.objects.filter(categories=instance.category)
        #     self.fields['materials'].queryset = MaterialPrice.objects.filter(categories=instance.category)

class PartAdmin(ImportExportModelAdmin):
    resource_class = PartResource
    list_display = ('category', 'purchase_part', 'part_number', 'size_length', 'size_width', 'size_thickness', 'volume', 'manufacturing_process', 'requires_mold', 'cavities_per_mold', 'material_utilization', 'recycle_usage_rate', 'production_cycle', 'operator_count', 'min_order_quantity', 'annual_demand')
    search_fields = ('category', 'purchase_part', 'part_number', 'supplier__supplier_code')

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'supplier':
    #         category = request.GET.get('category')
    #         if category:
    #             kwargs["queryset"] = Vendor.objects.filter(categories=category)
    #         else:
    #             kwargs["queryset"] = Vendor.objects.none()
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'materials':
    #         category = request.GET.get('category')
    #         if category:
    #             kwargs["queryset"] = MaterialPrice.objects.filter(categories=category)
    #         else:
    #             kwargs["queryset"] = MaterialPrice.objects.none()
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Part, PartAdmin)
