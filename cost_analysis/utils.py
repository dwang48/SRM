from material_price_info.models import MaterialPrice
from equipment_info.models import Equipment
from product_info.models import Product
from vendor_info.models import Vendor
from django.http import HttpResponse


# import requests

class ProcessCost:
    def __init__(self):
        pass

    #剪板
    @staticmethod
    def shearing_cost(设备现价值, 剩余折旧年数, 每小时产能, 设备功率, 电价, 操作员工资, 操作员人数):
        a = (设备现价值 / 剩余折旧年数) / 365 / 24 / 每小时产能
        b = (设备功率 * 电价) / 每小时产能
        c = (操作员工资 / 21.5) * 操作员人数 / 24 / 每小时产能
        return a + b + c

    #冲压
    @staticmethod
    def stamping_cost(设备现价值, 剩余折旧年数, 每小时产能, 每小时消耗量, 单价, 设备功率, 电价, 操作员工资, 操作员人数):
        e = (设备现价值 / 剩余折旧年数) / 365 / 24 / 每小时产能
        f = 每小时消耗量 * 单价 / 每小时产能
        g = (设备功率 * 电价) / 每小时产能
        h = (操作员工资 / 21.5) * 操作员人数 / 24 / 每小时产能
        return e + f + g + h

    #表面加工处理
    @staticmethod
    def surface_cost(单价每公斤, 产品净重):
        j = (单价每公斤 / 1000) * 产品净重
        return j
    

class PackagingCost:
    def __init__(self):
        pass

    @staticmethod
    def calculate(纸箱价格, 每箱包装量, PE袋价格, 每袋包装量, 操作员工资, 操作员人数, 包装每小时产能):
        k = 纸箱价格 / 每箱包装量
        l = PE袋价格 / 每袋包装量
        m = (操作员工资 / 21.5) * 操作员人数 / 24 / 包装每小时产能
        return k + l + m

class ShippingCost:
    def __init__(self):
        pass

    @staticmethod
    def calculate(每车运费, 每车箱数, 每箱包装量):
        return 每车运费 / 每车箱数 / 每箱包装量
    
def fullwidth_to_halfwidth(s):
    """Convert full-width characters to half-width characters."""
    result = []
    for char in s:
        code_point = ord(char)
        # Convert full-width characters to half-width characters
        if 0xFF01 <= code_point <= 0xFF5E:
            code_point -= 0xFEE0
        # Convert full-width space to half-width space
        elif code_point == 0x3000:
            code_point = 0x0020
        result.append(chr(code_point))
    return ''.join(result)


def calculate_shearing_cost(request):
    try:
        # Assuming that you get the equipment name and model from the request or some other source
        equipment_name = request.GET.get('equipment_name')
        equipment_model = request.GET.get('equipment_model')

        # Fetching the equipment information from the Equipment model
        equipment_info = Equipment.objects.get(设备名称=equipment_name, 设备型号=equipment_model)

        # Fetching other required parameters from the database
        设备现价值 = equipment_info.设备现价值
        剩余折旧年数 = equipment_info.剩余折旧年数
        每小时产能 = equipment_info.每小时产能
        设备功率 = equipment_info.设备功率
        电价 = equipment_info.电价
        操作员工资 = equipment_info.操作员工资
        操作员人数 = equipment_info.操作员人数

        # Calculate shearing cost using the extracted parameters
        shearing_cost_result = ProcessCost.shearing_cost(设备现价值, 剩余折旧年数, 每小时产能, 设备功率, 电价, 操作员工资, 操作员人数)

        # Render the result to a template or just return it as HttpResponse
        return HttpResponse(str(shearing_cost_result))

    except Equipment.DoesNotExist:
        return HttpResponse("设备信息不存在", status=400)
    except Exception as e:
        # Handle other potential exceptions
        return HttpResponse(f"发生了一个错误: {str(e)}", status=500)
