# from django.shortcuts import render
# from material_price_info.models import MaterialPrice
# from .models import CostAnalysis


# def calculate_material_cost(request):
#     if request.method == "POST":
#         selected_material = request.POST.get('selected_material')
#         material_info = MaterialPrice.objects.get(material_name=selected_material)
#         result = eval(formula.replace('原材料价格'，))
from material_price_info.models import MaterialPrice
from equipment_info.models import Equipment
from product_info.models import Product
from vendor_info.models import Vendor
from .utils import *
from .models import ProcessingMethod

from .models import CostAnalysis
from django.shortcuts import render
from django.http import JsonResponse

#转换全角到半角字符





def calculate_cost(request):
    materials = MaterialPrice.objects.all()
    result = None
    formula = ''
    substituted_formula = ''
    products = Product.objects.all()
    Equipments = Equipment.objects.all()
    processing_methods = ProcessingMethod.objects.all()

    if request.method == "POST":
        selected_product_id = request.POST.get('selected_product')
        product_info = Product.objects.get(id=selected_product_id)

        processing_methods = ProcessingMethod.objects.all()
        # selected_product_details = df_products[df_products['零件编号'] == product_info.part_number].iloc[0].to_dict()

        selected_material = request.POST.get('selected_material')
        product_gross_weight = float(request.POST.get('product_gross_weight'))
        product_net_weight = float(request.POST.get('product_net_weight'))

        material_info = MaterialPrice.objects.get(id=selected_material)

        # 使用你的公式进行计算
        dirty_formula = CostAnalysis.objects.get(产品描述="材料费").公式
        # 清理公式中的全角字符，并转换成半角字符
        formula = fullwidth_to_halfwidth(dirty_formula)
        # 计算
        substituted_formula = formula.replace('原材料价格', str(material_info.price)).replace('产品毛重', str(
            product_gross_weight)).replace('产品净重', str(product_net_weight)).replace('废料价格', str(material_info.scrap_price))
        result = eval(substituted_formula)

    return render(request, 'cost_analysis/calculate.html', {
        'processing_methods': processing_methods,
        'materials': materials,
        'products': products,
        'result': result,
        'original_formula': formula,
        'substituted_formula': substituted_formula,
    })






    



# def calculate_packaging_cost(request):
   