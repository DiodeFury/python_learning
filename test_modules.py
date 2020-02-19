# import ecommerce.shiping
# ecommerce.shiping.calc_shipping()
# from ecommerce import shiping
# shiping.calc_shipping()
import random          #调用系统库
for i in range(3):
    print(random.randint(10,20))
members = ['john', 'mosh', 'linda', 'marry']
print(random.choice(members))
class dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first,second


# dic = dice()
# print(dic.roll())

# from pathlib import Path
# path = Path()
# for file in path .glob('*.py'):
#     print(file)
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0,20,100)   # 创建一个列表
# plt.plot(x,np.sin(x))       # 对于每个点的sin值绘图
# plt.show()                  # 显示
