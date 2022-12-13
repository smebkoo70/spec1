import re

str_ = "Run level 3 (multi-user)"
number1 = re.findall("\d+", str_)  # 输出结果为列表
number2 = re.findall("[a-zA-Z]+", str_)  # 输出结果为列表
print(number1)
print(number2)
# 输出结果：['12', '333', '4']
