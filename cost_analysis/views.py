from material_price_info.models import *
from equipment_info.models import Equipment
from product_info.models import Product
from vendor_info.models import Vendor
from material_price_info.models import MaterialPrice
from .utils import *
from .models import Record
from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from django.apps import apps
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

class CostCalculator:
    def __init__(self, request, product, vendor):
        self.request = request
        self.product = product
        self.vendor = vendor

    def get_post_data(self, keys):
        data = {}
        for key in keys:
            value = self.request.POST.get(key, None)
            # Try to convert the value to a float, and if it fails, default to 0
            try:
                data[key] = float(value)
            except (TypeError, ValueError):
                data[key] = 0  # default value if conversion fails
        return data


    def calculate_process_cost(self, manufacturing_process, equipment):
        operator_count_key = f'operator_count_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}'
        qualification_rate_key = f'qualification_rate_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}'
        times_key = f'times_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}'
        hourly_capacity_key = f'hourly_capacity_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}'
        operator_wages_key = f'operator_wages_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}'
        # Extracting necessary data from request.POST
        keys = [operator_count_key,operator_wages_key,qualification_rate_key,times_key,hourly_capacity_key]
        data = self.get_post_data(keys)
        # 对于操作员工资
       
        if not data.get(operator_wages_key):
            operator_wages = self.vendor.operator_wages  # 使用默认值
        else:
            operator_wages = data.get(operator_wages_key)

        # 对于操作员人数
        if not data.get(operator_count_key):
            operator_count = self.product.operator_count  # 使用默认值
        else:
            operator_count = data.get(operator_count_key)

        # 对于合格率
        if not data.get(qualification_rate_key):
            qualification_rate = 100  # 使用默认值
        else:
            qualification_rate = data.get(qualification_rate_key)

        # 对于次数
        if not data.get(times_key):
            times = 1  # 使用默认值
        else:
            times = data.get(times_key)

        # 对于每小时产能
        if not data.get(hourly_capacity_key):
            hourly_capacity = self.product.hourly_capacity  # 使用默认值
        else:
            hourly_capacity = data.get(hourly_capacity_key)
        
        if manufacturing_process == '表面加工处理':
            params = {
                '单价每公斤': 3,
                '产品净重': self.product.part_net_weight,
            }
            return ProcessCost.surface_cost(**params)
        
        params = {
            '设备现价值': equipment.current_value,
            '剩余折旧年数': equipment.remaining_depreciation_years,
            '每小时产能': hourly_capacity,
            '设备功率': equipment.power_kw,
            '辅助功率1': equipment.auxiliary_power_a_kw,
            '辅助功率2': equipment.auxiliary_power_b_kw,
            '辅助功率3': equipment.auxiliary_power_c_kw,
            '电价': self.vendor.electricity_price,
            '操作员工资': operator_wages,
            '操作员人数': operator_count,
            '合格率': qualification_rate,
            '次数': times,
            '每小时耗水量': equipment.water_consumption,
            '水单价': self.vendor.water_price,
            '每小时耗气量': equipment.gas_consumption,
            '气单价': self.vendor.gas_price,
            '每小时其他资源耗用量': equipment.other_resource_consumption,
            '其他单价': equipment.other_resource_price,
            '每小时附加资源耗用量': equipment.additional_resource_consumption,
            '附加单价': equipment.additional_resource_price,
            '附加资源2': equipment.additional_resource_consumption2,
            '附加单价2': equipment.additional_resource_price2,
            '附加资源3': equipment.additional_resource_consumption3,
            '附加单价3': equipment.additional_resource_price3
        }

        print(params)
        return ProcessCost.有材料消耗类成本(**params)

        # ... (handle other manufacturing processes if needed)

    def calculate_total_material_cost(self, selected_material_ids,request):
        """
        计算选定材料的成本。

        参数:
        - selected_material_ids: 选中的材料的ID列表。
        """
        total_material_cost = 0

        for material_id in selected_material_ids:
            # 假设有一个方法能根据material_id取得材料的信息，如价格等
            material = MaterialPrice.objects.get(id=material_id)  # 请根据实际情况调整这里的查询

            # 从请求中获取材料所需参数的数据
            weight_or_count = request.POST.get(f'weight_or_count_{material_id}')
            net_weight_input = request.POST.get(f'net_weight_{material_id}')
            consumption_coefficient = request.POST.get(f'consumption_coefficient_{material_id}')

            # 处理可能的空值，设置默认值或进行类型转换
            # 获取必要的参数
            产品毛重 =  float(weight_or_count)# 需要从某处获取或定义这个值
            if not net_weight_input:
                产品净重 = float(weight_or_count)  # 假设默认净重与毛重相同
            else:
                产品净重 = float(net_weight_input) 
            废料价格 = material.scrap_price# 需要从某处获取或定义这个值
            系数 =  float(consumption_coefficient)# 需要从某处获取或定义这个值

            # 计算当前材料的成本并累加至总成本
            total_material_cost += MaterialCost.calculate(产品毛重, material.price, 产品净重, 废料价格, 系数)

        return total_material_cost

def calculate_processing_cost(request):
    # Get selected equipment data list from request
    selected_equipment_data_list = request.POST.getlist('selected_equipment')

    # Get selected product ID from request and fetch the product object
    selected_product_id = request.POST.get('selected_product')
    product = Product.objects.get(id=selected_product_id)

    # Fetch the vendor object using the supplier name from the product object
    vendor = Vendor.objects.get(supplier_code=product.supplier_code)

    # Create a calculator instance with the request, product, and vendor objects
    calculator = CostCalculator(request, product, vendor)

    total_cost = 0  # Initialize the total cost to 0

    for selected_equipment_data in selected_equipment_data_list:
        manufacturing_process, equipment_name, equipment_model = selected_equipment_data.split('|')

        # Fetch the equipment object using the equipment name and model
        equipment = Equipment.objects.get(
            manufacturing_process=manufacturing_process,
            equipment_name=equipment_name,
            equipment_model=equipment_model
        )

        # Calculate the cost for the current equipment using the calculator instance
        cost = calculator.calculate_process_cost(manufacturing_process, equipment)
        total_cost += cost  # Accumulate the total cost

        print(f"当前选项的成本: {cost}")  # Print the cost for the current equipment

    print(f"总成本: {total_cost}")  # Print the total cost
    return total_cost  # Return the total cost


def is_admin(user):
    return user.is_authenticated and user.is_staff

# @user_passes_test(is_admin)
def calculate_cost(request):
    if not is_admin(request.user):
        return HttpResponseForbidden()
    selected_equipment_data_list = request.POST.getlist('selected_equipment')
    category = request.path_info.split('/')[2]
    
    if request.method == 'GET':
        category_name = request.GET.get('name')
    else:
        category_name = request.POST.get('name')
    
    # print(category_name)

    model_name = f"MaterialPrice"
    # print(model_name)

    # 动态获取模型
    try:
        ModelClass = apps.get_model('material_price_info', model_name)
    except LookupError:
        raise ImproperlyConfigured(f"No model found for category: {category}")
    
    
    #对应材料费，管理费，加工费，包装费
    processing_details = ''
    material_result = 0
    shipping_result = 0
    processing_result = 0
    packaging_result = 0
    managing_result = 0
    profit = 0
    total_cost = 0
    material_coefficient = 1
    # selected_methods = []
    management_fee_percentage = 0
    profit_margin_percentage = 0
    
    products = Product.objects.filter(categories=category_name)
    # products = Product.objects.all()
    # Equipments = Equipment.objects.all()
    manufacturing_process = Equipment.objects.filter(category=category_name).values_list('manufacturing_process',flat=True).distinct()
    # manufacturing_process = Equipment.objects.values_list('manufacturing_process',flat=True).distinct()
    manufacturing_data = []
    all_materials = ModelClass.objects.filter(categories=category_name)

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
        additional_material_cost = float(request.POST.get('additional_material_cost', 0))
        additional_packaging_cost = float(request.POST.get('additional_packaging_cost', 0))
        additional_transport_cost = float(request.POST.get('additional_transport_cost', 0))
        additional_process_cost = float(request.POST.get('additional_process_cost', 0))
        selected_product_id = request.POST.get('selected_product')
        product_info = Product.objects.get(id=selected_product_id)
        # vendor_info = Vendor.objects.get(supplier_name=product_info.supplier)
        material_info = ModelClass.objects.get(material_name=product_info.material_name,material_grade = product_info.material_grade)
        material_coefficient = float(request.POST.get('material_coefficient'))
        # selected_material = request.POST.get('selected_material')

        product_gross_weight = product_info.part_gross_weight
        management_fee_percentage = product_info.management_fee_percentage
        profit_margin_percentage = product_info.profit_margin_percentage
       
        product_net_weight = product_info.part_net_weight



        # 计算材料费
        material_result = MaterialCost.calculate(product_gross_weight,material_info.price,product_net_weight,material_info.scrap_price,material_coefficient)
        
        material_result += additional_material_cost

        material_result = round(material_result,4)
        # material_result_rounded = round(material_result,3)

        #计算包装费
        packaging_result = PackagingCost.calculate(product_info.carton_price,product_info.pieces_per_carton,product_info.pe_bag_price,product_info.pieces_per_bag)
        packaging_result += additional_packaging_cost
        packaging_result = round(packaging_result,4)
        # packaging_result_rounded = round(packaging_result,3)

        #计算运输费
        shipping_result = ShippingCost.calculate(product_info.transport_fee_per_vehicle,product_info.cartons_per_vehicle)
        shipping_result += additional_transport_cost
        shipping_result = round(shipping_result,4)

        #计算加工费
        processing_result = calculate_processing_cost(request)
        # material_result_rounded = round(material_result,3)
        processing_result += additional_process_cost
        processing_result = round(processing_result,4)

        #显示加工费明细
        processing_details += ", ".join(selected_equipment_data_list)

        subtotal = material_result + packaging_result + shipping_result + processing_result
        # print("小记：" + str(subtotal))
        #计算管理费
        management_fee_percentage = product_info.management_fee_percentage / 100
        managing_result = management_fee_percentage * subtotal
        managing_result = round(managing_result,4)

        #计算利润
        profit_margin_percentage = product_info.profit_margin_percentage/100
        # print(profit_margin_percentage)
        profit = profit_margin_percentage * (1 + management_fee_percentage)*subtotal
        profit = round(profit,4)



        #计算总费用
        total_cost = (material_result + packaging_result + shipping_result + processing_result)*(1+management_fee_percentage)*(1+profit_margin_percentage)*1.13
        total_cost = round(total_cost,4)

        
    if category in ['zhusu','pentu']:
        template_name = f"cost_analysis/calculate_{category}.html"
    else:
        template_name = "cost_analysis/calculate.html"

    return render(request, template_name, {
        'category': category,
        'manufacturing_data': manufacturing_data,
        'products': products,
        'material_result': material_result,
        'shipping_result': shipping_result,
        'packaging_result': packaging_result,
        'processing_result': processing_result,
        'total_cost': total_cost,
        'managing_result':managing_result,
        'profit':profit,
        'material_coefficient': material_coefficient,
        "all_materials": all_materials
    })


@csrf_exempt
def save_record(request):
    if request.method == "POST":
        print("Received POST data:", request.POST)
        try:
            new_record = Record(
                产品编号=request.POST.get('product_info_part_number'),
                材料费=float(request.POST.get('material_result', '0.0')),
                加工费=float(request.POST.get('processing_result', '0.0')),
                包装费=float(request.POST.get('packaging_result', '0.0')),
                运输费=float(request.POST.get('shipping_result', '0.0')),
                管理费比例=float(request.POST.get('managing_result', '0.0')),
                利润率=float(request.POST.get('profit', '0.0')),
                总成本=float(request.POST.get('total_cost', '0.0'))
            )
            new_record.save()
            return JsonResponse({"status": "success"})
        except ValueError:
            return JsonResponse({"status": "error", "message": "Invalid input data"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request"})

    
