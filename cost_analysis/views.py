from material_price_info.models import *
from equipment_info.models import Equipment
from product_info.models import Product
from vendor_info.models import Vendor
from .utils import *
from .models import Record
from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ImproperlyConfigured
from django.apps import apps

def calculate_processing_cost(request):

    selected_equipment_data_list = request.POST.getlist('selected_equipment')
    selected_product_id = request.POST.get('selected_product')
    product = Product.objects.get(id=selected_product_id)
    vendor = Vendor.objects.get(supplier_name=product.supplier)

    method_mapping = {
        #垂重
        '剪切': ProcessCost.无材料消耗类成本,
        '冲压': ProcessCost.有材料消耗类成本,
        '冷镦': ProcessCost.有材料消耗类成本,
        '表面加工处理': ProcessCost.surface_cost,
        #磁铁
        '真空感应速凝炉': ProcessCost.无材料消耗类成本,
        '气流磨':ProcessCost.无材料消耗类成本,
        '磁场成型压机':ProcessCost.无材料消耗类成本,
        '烧结炉':ProcessCost.无材料消耗类成本,
        '等静压炉':ProcessCost.无材料消耗类成本,
        '多线成型机':ProcessCost.无材料消耗类成本,
        '双面磨床':ProcessCost.无材料消耗类成本,
        '震动抛光盘':ProcessCost.无材料消耗类成本,
        '电镀槽': ProcessCost.无材料消耗类成本,
        '充磁机': ProcessCost.无材料消耗类成本,
        #弹簧
        '卷簧机': ProcessCost.无材料消耗类成本,
        '回火炉': ProcessCost.无材料消耗类成本,

    }

    total_cost = 0  # 初始化总成本为0

    for selected_equipment_data in selected_equipment_data_list:
        manufacturing_process, equipment_name, equipment_model = selected_equipment_data.split('|')
        print('选中的加工方法：' + manufacturing_process)

        equipment = Equipment.objects.get(
            manufacturing_process=manufacturing_process,
            equipment_name=equipment_name,
            equipment_model=equipment_model
        )

        method_params = {
            '冷镦':{
                '设备现价值': equipment.current_value,
                '剩余折旧年数': equipment.remaining_depreciation_years,
                '每小时产能': product.hourly_capacity,
                '每小时消耗量': equipment.lubricating_oil_consumption,
                '单价': equipment.oil_price_per_kg,
                '设备功率': equipment.power_kw,
                '电价': vendor.electricity_price,
                '操作员工资': vendor.operator_wages,
                '操作员人数': product.operator_count,
            },
            '剪切': {
                '设备现价值': equipment.current_value,
                '剩余折旧年数': equipment.remaining_depreciation_years,
                '每小时产能': product.hourly_capacity,
                '设备功率': equipment.power_kw,
                '电价': vendor.electricity_price,
                '操作员工资': vendor.operator_wages,
                '操作员人数': product.operator_count,
            },
            '冲压': {
                '设备现价值': equipment.current_value,
                '剩余折旧年数': equipment.remaining_depreciation_years,
                '每小时产能': product.hourly_capacity,
                '每小时消耗量': equipment.lubricating_oil_consumption,
                '单价': equipment.oil_price_per_kg,
                '设备功率': equipment.power_kw,
                '电价': vendor.electricity_price,
                '操作员工资': vendor.operator_wages,
                '操作员人数': product.operator_count,
            },
            '表面加工处理': {
                '单价每公斤': 3,
                '产品净重': product.part_net_weight,
            },
        }

        if manufacturing_process in method_mapping:
            method = method_mapping[manufacturing_process]
            cost = method(**method_params[manufacturing_process])
            total_cost += cost
            print("当前选项的成本: " + str(cost))

    print("总成本: " + str(total_cost))
    return total_cost


def calculate_cost(request):
    category = request.path_info.split('/')[2]

    # 将首字母大写并拼接到 'MaterialPrice'
    model_name = f"{category.capitalize()}MaterialPrice"
    print(model_name)

    # 动态获取模型
    try:
        ModelClass = apps.get_model('material_price_info', model_name)
    except LookupError:
        raise ImproperlyConfigured(f"No model found for category: {category}")

    # materials = ModelClass.objects.all()
    
    #对应材料费，管理费，加工费，包装费
    processing_details = ''
    material_result = 0
    shipping_result = 0
    processing_result = 0
    packaging_result = 0
    total_cost = 0
    # selected_methods = []
    management_fee_percentage = 0
    profit_margin_percentage = 0
    
    products = Product.objects.all()
    Equipments = Equipment.objects.all()
    manufacturing_process = Equipment.objects.values_list('manufacturing_process',flat=True).distinct()

    manufacturing_data = []

    for process in manufacturing_process:
        process_data = {
            'process': process,
            'equipments': []
        }
        
        # Get all equipment names for this manufacturing process
        names_for_process = Equipment.objects.filter(manufacturing_process=process).values_list('equipment_name', flat=True).distinct()
        
        for name in names_for_process:
            equipment_data = {
                'name': name,
                'models': []
            }
            
            # Get all equipment models for this equipment name
            models_for_name = Equipment.objects.filter(manufacturing_process=process, equipment_name=name).values_list('equipment_model', flat=True).distinct()
            equipment_data['models'] = list(models_for_name)
            
            process_data['equipments'].append(equipment_data)
        
        manufacturing_data.append(process_data)

    if request.method == "POST":
        selected_product_id = request.POST.get('selected_product')
        product_info = Product.objects.get(id=selected_product_id)
        vendor_info = Vendor.objects.get(supplier_name=product_info.supplier)
        material_info = ModelClass.objects.get(material_name=product_info.material_name,material_grade = product_info.material_grade)

        # selected_material = request.POST.get('selected_material')

        product_gross_weight = product_info.part_gross_weight
        management_fee_percentage = product_info.management_fee_percentage
        profit_margin_percentage = product_info.profit_margin_percentage
       
        product_net_weight = product_info.part_net_weight



        #计算材料费
        # material_info = ModelClass.objects.get(id=selected_material)

        # 计算材料费
        material_result = MaterialCost.calculate(product_gross_weight,material_info.price,product_net_weight,material_info.scrap_price)
        # material_result_rounded = round(material_result,3)

        #计算包装费
        packaging_result = PackagingCost.calculate(product_info.carton_price,product_info.pieces_per_carton,product_info.pe_bag_price,product_info.pieces_per_bag,vendor_info.operator_wages,product_info.operator_count,product_info.hourly_capacity)
        # packaging_result_rounded = round(packaging_result,3)

        #计算运输费
        shipping_result = ShippingCost.calculate(product_info.transport_fee_per_vehicle,product_info.cartons_per_vehicle,product_info.pieces_per_carton)

        #计算加工费
        processing_result = calculate_processing_cost(request)
        # material_result_rounded = round(material_result,3)

        #显示加工费明细
        # processing_details += ", ".join(selected_methods)


        #计算总费用
        total_cost = (material_result + packaging_result + shipping_result + processing_result)*(1+management_fee_percentage/100)*(1+profit_margin_percentage/100)*1.13



        #保存到计算record中的数据库中
        # 创建新的记录实例
        new_record = Record(
        产品编号=product_info.part_number,  # 假设你已经提取了product_info
        材料费=material_result,  # 你之前计算的值
        加工费=processing_result,
        加工明细=processing_details,
        运输费=shipping_result,
        包装费=packaging_result,
        管理费比例=management_fee_percentage,
        利润率=profit_margin_percentage,
        总成本=total_cost  # 你之前计算的值
        )
        new_record.save()

    return render(request, 'cost_analysis/calculate.html', {
        'category': category,
        'manufacturing_data': manufacturing_data,
        'products': products,
        'material_result': material_result,
        'shipping_result': shipping_result,
        'packaging_result': packaging_result,
        'processing_result': processing_result,
        'total_cost': total_cost,
        # 'selected_methods':selected_methods,
    })


