"""
Create by Killer at 2019-05-07 15:13
"""

# 处理货币值
from decimal import Decimal

tax_rate = Decimal('7.25')/Decimal(100)
purchase_amount = Decimal('2.95')
print(tax_rate * purchase_amount)

# 使用对象量化数据
penney = Decimal('0.01')
total_amount = purchase_amount + tax_rate * purchase_amount
print(total_amount.quantize(penney))

# 分数计算
# 当计算中含有精确分数值时，可以使用fractions模块
from fractions import Fraction

# 由字符串、整数或整数对创建Fraction对象。
sugur_cups = Fraction('2.5')
scale_factor = Fraction(5/8)
print(sugur_cups * scale_factor)

# floor除法
total_seconds = 7385
hours = total_seconds // 3600
remaning_seconds = total_seconds % 3600

minutes = remaning_seconds // 60
seconds = remaning_seconds % 60
print(hours, minutes, seconds)

# 使用divmod()函数
hours, remaning_seconds = divmod(total_seconds, 3600)

minutes, seconds = divmod(remaning_seconds, 60)
print(hours, minutes, seconds)

# 字符串 子字符串 分隔符
title = "Recipe 5: Rewriting, and the Immutable String"

# 切片字符串
# 查找边界
colon_position = title.index(":")

# 选择子字符串
discard_text, post_colon_text = title[:colon_position], title[colon_position+1:]
print(discard_text)
print(post_colon_text)

# 使用 partition()和手动切片
pre_colon_text, _, post_colon_text = title.partition(":")
print(pre_colon_text)
print(post_colon_text)

import re

ingredient = "Kumquat: 2 cpus"
# 使用正则表达式
pattern_text = r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)'

# \w+替换words \d+替换digits \s+替换单个空格  ?p<name>标识需要提取的数据
pattern = re.compile(pattern_text)
# 编译模式

match = pattern.match(ingredient)
print(match.groups())
print(match.group('ingredient')) # 根据标识获取

# format_map 格式化复杂的字符串
class Summary:
    def __init__(self, id, location, min_temp, max_temp, precipitation):
        self.id = id
        self.location = location
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.precipitation = precipitation

    def __str__(self):
        return '{id:3s}    : {location:19s} :     {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(vars(self)) # vars() 创建属性字典

s = Summary('IAD', 'Dulles Intl Airport', 13, 32, 0.4)

print(s)


