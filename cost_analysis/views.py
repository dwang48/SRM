from material_price_info.models import *
from equipment_info.models import Equipment
from product_info.models import Product
from vendor_info.models import Vendor
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
            data[key] = float(value) if value and value.isnumeric() else 0
        return data

    def calculate_process_cost(self, manufacturing_process, equipment):

        # Extracting necessary data from request.POST
        keys = [
            f"hourly_capacity_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}",
            f"qualification_rate_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}",
            f"times_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}",
            f"operator_count_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}",
            f"operator_wages_{manufacturing_process}|{equipment.equipment_name}|{equipment.equipment_model}"
        ]
        data = self.get_post_data(keys)
        
        if manufacturing_process == '表面加工处理':
            params = {
                '单价每公斤': 3,
                '产品净重': self.product.part_net_weight,
            }
            return ProcessCost.surface_cost(**params)
            
        # Setting up the parameters for ProcessCost.calculate
        params = {
            '设备现价值': equipment.current_value,
            '剩余折旧年数': equipment.remaining_depreciation_years,
            '每小时产能': data.get('hourly_capacity', 1),
            '设备功率': equipment.power_kw,
            '电价': self.vendor.electricity_price,
            '操作员工资': data.get('operator_wages', self.vendor.operator_wages),
            '操作员人数': data.get('operator_count', self.product.operator_count),
            '合格率': data.get('qualification_rate', 1),
            '次数': data.get('times', 1)
        }
        return ProcessCost.calculate(**params)
        # ... (handle other manufacturing processes if needed)


def calculate_processing_cost(request):
    # Get selected equipment data list from request
    selected_equipment_data_list = request.POST.getlist('selected_equipment')

    # Get selected product ID from request and fetch the product object
    selected_product_id = request.POST.get('selected_product')
    product = Product.objects.get(id=selected_product_id)

    # Fetch the vendor object using the supplier name from the product object
    vendor = Vendor.objects.get(supplier_name=product.supplier)

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
    
    print(category_name)

    model_name = f"MaterialPrice"
    print(model_name)

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
    manufacturing_process = Equipment.objects.filter(purchase_category=category_name).values_list('manufacturing_process',flat=True).distinct()
    # manufacturing_process = Equipment.objects.values_list('manufacturing_process',flat=True).distinct()
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
        material_result = round(material_result,4)
        # material_result_rounded = round(material_result,3)

        #计算包装费
        packaging_result = PackagingCost.calculate(product_info.carton_price,product_info.pieces_per_carton,product_info.pe_bag_price,product_info.pieces_per_bag)
        packaging_result = round(packaging_result,4)
        # packaging_result_rounded = round(packaging_result,3)

        #计算运输费
        shipping_result = ShippingCost.calculate(product_info.transport_fee_per_vehicle,product_info.cartons_per_vehicle)
        shipping_result = round(shipping_result,4)

        #计算加工费
        processing_result = calculate_processing_cost(request)
        # material_result_rounded = round(material_result,3)
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

        # new_record = Record(
        # 产品编号=product_info.part_number,
        # 材料费=material_result,
        # 加工费=processing_result,
        # 加工明细=processing_details,
        # 运输费=shipping_result,
        # 包装费=packaging_result,
        # 管理费比例=management_fee_percentage,
        # 利润率=profit_margin_percentage,
        # 总成本=total_cost 
        # )
        # new_record.save()

    return render(request, 'cost_analysis/calculate.html', {
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
        # 'selected_methods':selected_methods,
    })


@csrf_exempt
def save_record(request):
    if request.method == "POST":
        new_record = Record(
            产品编号=request.POST.get('product_info_part_number'),
            材料费=request.POST.get('material_result'),
            加工费=request.POST.get('processing_result'),
            包装费=request.POST.get('packaging_result'),
            运输费=request.POST.get('shipping_result'),
            管理费比例=request.POST.get('managing_result'),
            利润率=request.POST.get('profit'),
            总成本=request.POST.get('total_cost')
        )
        new_record.save()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})

