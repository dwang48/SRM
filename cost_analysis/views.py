from material_price_info.models import MaterialPrice
from equipment_info.models import Equipment
from product_info.models import Product
from vendor_info.models import Vendor
from .utils import *
from .models import ProcessingMethod,Record
from django.shortcuts import render
from django.http import JsonResponse

def calculate_processing_cost(request):

    selected_methods = request.POST.getlist('processing_methods[]')
    method_mapping ={
        '剪板': ProcessCost.shearing_cost,
        '冲压': ProcessCost.stamping_cost,
        '表面加工处理': ProcessCost.surface_cost,
    }

    #参数字典
    method_params = {
    '剪板': [
        ('设备现价值', 'Any'),
        ('剩余折旧年数', 'Any'),
        ('每小时产能', 'Any'),
        ('设备功率', 'Any'),
        ('电价', 'Any'),
        ('操作员工资', 'Any'),
        ('操作员人数', 'Any'),
    ],
    '冲压': [
        ('设备现价值', 'Any'),
        ('剩余折旧年数', 'Any'),
        ('每小时产能', 'Any'),
        ('每小时消耗量', 'Any'),
        ('单价', 'Any'),
        ('设备功率', 'Any'),
        ('电价', 'Any'),
        ('操作员工资', 'Any'),
        ('操作员人数', 'Any'),
    ],
    '表面加工处理': [
        ('单价每公斤', 'Any'),
        ('产品净重', 'Any'),
    ],
}

    print("选中的加工方法: " + ", ".join(selected_methods))
    total_cost = 0
    for method in selected_methods:
        if method in method_mapping:
            # 为每个方法提取参数
            params = {name: request.POST.get(param_name) for name, param_name in method_params[method]}
            
            # 调用相应的方法
            cost = method_mapping[method](**params)
            total_cost += cost
    return total_cost


def calculate_cost(request):
    materials = MaterialPrice.objects.all()
    
    #对应材料费，管理费，加工费，包装费
    material_result = 0
    shipping_result = 0
    processing_result = 0
    packaging_result = 0
    total_cost = 0
    selected_methods = []
    management_fee_percentage = 0
    profit_margin_percentage = 0
    
    formula = ''
    substituted_formula = ''
    products = Product.objects.all()
    Equipments = Equipment.objects.all()
    processing_methods = ProcessingMethod.objects.all()

    if request.method == "POST":
        selected_methods = request.POST.getlist('processing_methods[]')
        selected_product_id = request.POST.get('selected_product')
        print(selected_product_id)
        product_info = Product.objects.get(id=selected_product_id)
        vendor_info = Vendor.objects.get(supplier_name=product_info.supplier)

        processing_methods = ProcessingMethod.objects.all()

        selected_material = request.POST.get('selected_material')
        print("Selected Material ID:", selected_material)

        product_gross_weight = product_info.part_gross_weight
        management_fee_percentage = product_info.management_fee_percentage
        profit_margin_percentage = product_info.profit_margin_percentage
       
        product_net_weight = product_info.part_net_weight
        print('毛重：' + str(product_gross_weight))
        print('净重：' + str(product_net_weight))



        #计算材料费
        material_info = MaterialPrice.objects.get(id=selected_material)

        # 计算材料费
        material_result = MaterialCost.calculate(product_gross_weight,material_info.price,product_net_weight,material_info.scrap_price)


        #计算包装费
        packaging_result = PackagingCost.calculate(product_info.carton_price,product_info.pieces_per_carton,product_info.pe_bag_price,product_info.pieces_per_bag,vendor_info.operator_wages,product_info.operator_count,product_info.hourly_capacity)

        #计算运输费
        shipping_result = ShippingCost.calculate(product_info.transport_fee_per_vehicle,product_info.cartons_per_vehicle,product_info.pieces_per_carton)


        #计算加工费
        processing_result = calculate_processing_cost(request)

        #计算总费用
        total_cost = (material_result + packaging_result + shipping_result + processing_result)*(1+management_fee_percentage/100)*(1+profit_margin_percentage/100)*1.13



        #保存到计算record中的数据库中
        # 创建新的记录实例
        new_record = Record(
        产品编号=product_info.part_number,  # 假设你已经提取了product_info
        材料费=material_result,  # 你之前计算的值
        加工费=processing_result,
        运输费=shipping_result,
        包装费=packaging_result,
        管理费比例=management_fee_percentage,
        利润率=profit_margin_percentage,
        总成本=total_cost  # 你之前计算的值
        )
        new_record.save()

    return render(request, 'cost_analysis/calculate.html', {
        'processing_methods': processing_methods,
        'materials': materials,
        'products': products,
        'material_result': material_result,
        'total_cost': total_cost,
        'shipping_result': shipping_result,
        'packaging_result': packaging_result,
        'processing_result': processing_result,
        'total_cost': total_cost,
        'selected_methods':selected_methods,
    })


