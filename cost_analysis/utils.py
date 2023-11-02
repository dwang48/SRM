from material_price_info.models import *
from equipment_info.models import Equipment
from product_info.models import Product
from vendor_info.models import Vendor
from django.http import HttpResponse


# import requests

class MaterialCost:
    @staticmethod
    def calculate(产品毛重, 原材料价格, 产品净重, 废料价格,系数):
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
        #原材料合格率
        原材料成本 = 产品毛重 * (原材料价格 / 1000000) - (产品毛重 - 产品净重) * (废料价格 / 1000000)
        return 原材料成本 * 系数


    @staticmethod
    def calculate2(materials):
        total_cost = 0
        for material in materials:
            material_cost = material['gross_weight'] * (material['price'] / 1000000) - (material['gross_weight'] - material['net_weight']) * (material['scrap_price'] / 1000000)
            total_cost += material_cost * material['coefficient']
        return total_cost




class ProcessCost:
    def __init__(self):
        pass

    #垂重
    #无材料消耗类，仅考虑电费
    @staticmethod
    def calculate(设备现价值, 剩余折旧年数, 每小时产能, 设备功率, 电价, 操作员工资, 操作员人数,合格率,次数):
        真实产能 = 每小时产能 * 合格率 / 100
        a = (设备现价值 / 剩余折旧年数) / 365 / 24 / 真实产能
        b = (设备功率 * 电价) / 真实产能
        c = (操作员工资 / 21.5) * 操作员人数 / 24 / 真实产能
        # print(次数)s
        #print(f"Inside method, times: {次数}")
        return (a + b + c) * 次数

    #有材料消耗类
    @staticmethod
    def 有材料消耗类成本(设备现价值, 剩余折旧年数, 每小时产能, 设备功率, 辅助功率1,辅助功率2,辅助功率3,电价, 操作员工资, 操作员人数,合格率,次数,每小时耗水量,水单价,每小时耗气量,气单价,每小时其他资源耗用量,其他单价,每小时附加资源耗用量,附加单价,附加资源2,附加单价2,附加资源3,附加单价3):
        真实产能 = 每小时产能 * 合格率 / 100
        e = (设备现价值 / 剩余折旧年数) / 365 / 24 / 真实产能
        f1 = 每小时耗水量 * 水单价 / 真实产能
        f2 = 每小时耗气量 * 气单价 / 真实产能
        f3 = 每小时其他资源耗用量 * 其他单价 / 真实产能
        f4 = 每小时附加资源耗用量 * 附加单价 / 真实产能
        f5 = 附加单价2 * 附加资源2 / 真实产能
        f6 = 附加单价3 * 附加资源3 / 真实产能

        总功率 = 设备功率 + 辅助功率1 + 辅助功率2 + 辅助功率3
        g = (总功率 * 电价) / 真实产能
        h = (操作员工资 / 26) * 操作员人数 / 10 / 真实产能
        

        return (e + f1 +f2 +f3 + f4 + f5 + f6 + g + h) * 次数

    #表面加工处理
    @staticmethod
    def surface_cost(单价每公斤, 产品净重):
        j = (单价每公斤 / 1000) * 产品净重
        # print("表面加工价格：" + str(j))
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
    def calculate(每车运费, 每车货物):
        return 每车运费 / 每车货物
    

    
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



    
