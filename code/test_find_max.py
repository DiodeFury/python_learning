#模块调用
import find_max
#第一种用法
number1 = [0, 4, 7, 1, 2, 3, 10, 5]
find_max.find(number1)
#第二种用法
from find_max import find
number2 = [8, 3, 3, 2, 34]
find(number2)

#其实python 带有max（）函数
print(max(number2))
