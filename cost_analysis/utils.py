from material_price_info.models import *
from equipment_info.models import Equipment
from product_info.models import Product
from vendor_info.models import Vendor
from django.http import HttpResponse


# import requests

class MaterialCost:
    @staticmethod
    def calculate(产品毛重, 原材料价格, 产品净重, 废料价格):
        """
        根据提供的公式计算原材料成本。

        参数：
        - 产品毛重: 商品的总重量
        - 原材料价格: 原材料的单位价格
        - 产品净重: 商品的净重量
        - 废料价格: 废料的单位价格

        返回：
        - 原材料成本: 计算出的原材料成本
        """
        原材料成本 = 产品毛重 * (原材料价格 / 1000000) - (产品毛重 - 产品净重) * (废料价格 / 1000000)
        return 原材料成本




class ProcessCost:
    def __init__(self):
        pass

    #垂重
    #无材料消耗类，仅考虑电费
    @staticmethod
    def 无材料消耗类成本(设备现价值, 剩余折旧年数, 每小时产能, 设备功率, 电价, 操作员工资, 操作员人数,合格率,次数):
        真实产能 = 每小时产能 * 合格率 / 100
        a = (设备现价值 / 剩余折旧年数) / 365 / 24 / 真实产能
        b = (设备功率 * 电价) / 真实产能
        c = (操作员工资 / 21.5) * 操作员人数 / 24 / 真实产能
        # print(次数)
        #print(f"Inside method, times: {次数}")
        return (a + b + c) * 次数

    #有材料消耗类
    @staticmethod
    def 有材料消耗类成本(设备现价值, 剩余折旧年数, 每小时产能, 每小时消耗量, 单价, 设备功率, 电价, 操作员工资, 操作员人数,合格率,次数):
        真实产能 = 每小时产能 * 合格率 / 100
        e = (设备现价值 / 剩余折旧年数) / 365 / 24 / 真实产能
        f = 每小时消耗量 * 单价 / 真实产能
        g = (设备功率 * 电价) / 真实产能
        h = (操作员工资 / 21.5) * 操作员人数 / 24 / 真实产能
        # print(次数)
        # print(f"Inside method, times: {次数}")
        return (e + f + g + h) * 次数

    #表面加工处理
    @staticmethod
    def surface_cost(单价每公斤, 产品净重):
        j = (单价每公斤 / 1000) * 产品净重
        return j





class PackagingCost:
    def __init__(self):
        pass

    @staticmethod
    def calculate(纸箱价格, 每箱包装量, PE袋价格, 每袋包装量):
        k = 纸箱价格 / 每箱包装量
        l = PE袋价格 / 每袋包装量 / 每箱包装量
        # m = (操作员工资 / 21.5) * 操作员人数 / 24 / 包装每小时产能
        return k + l

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






    
