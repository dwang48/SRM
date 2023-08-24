# from django.shortcuts import render
# from material_price_info.models import MaterialPrice
# from .models import CostAnalysis



# def calculate_material_cost(request):
#     if request.method == "POST":
#         selected_material = request.POST.get('selected_material')
#         material_info = MaterialPrice.objects.get(material_name=selected_material)
#         result = eval(formula.replace('原材料价格'，))
from material_price_info.models import MaterialPrice
from .models import CostAnalysis
from django.shortcuts import render

def calculate_material_cost(request):
    materials = MaterialPrice.objects.all()
    result = None

    if request.method == "POST":
        selected_material = request.POST.get('selected_material')
        product_gross_weight = float(request.POST.get('product_gross_weight'))
        product_net_weight = float(request.POST.get('product_net_weight'))

        material_info = MaterialPrice.objects.get(id=selected_material)

        # 使用你的公式进行计算
        formula = CostAnalysis.objects.get(product_description="材料费").公式
        result = eval(formula.replace('原材料价格', str(material_info.price))
                              .replace('产品毛重', str(product_gross_weight))
                              .replace('产品净重', str(product_net_weight))
                              .replace('废料价格', str(material_info.scrap_price)))

    return render(request, 'cost_analysis/calculate.html', {
        'materials': materials,
        'result': result
    })
