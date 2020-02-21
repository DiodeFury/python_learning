#pratice 1
# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# 1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去
# 掉不满足条件的排列。

'''
for i in range(1,5):
    for j in range (1,5):
        for k in range (1,5):
            if (i!=k) and (i!=j)and(k!=j):
                print(i,j,k)
'''

#prctice2
#输入年份判断是不是闰年
'''
year = int(input(('请输入年份:')))
is_leap = (year % 4 == 0 and year % 100 == 0)
print(is_leap)
'''

#practice3
#输入圆的半径计算计算周长和面积。
'''
import math
r = float(input("请输入圆的半径:"))
l = 2 * math.pi * r
s = r**2 * math.pi
print('周长：%f' % l)
print('面积：%f' % s)
'''

#pratice4
#如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
# 70分-80分（不含80分）输出C；
# 60分-70分（不含70分）输出D；
# 60分以下输出E。
'''
score = float(input('请输入成绩：'))
if score >= 90:
    print("A")
elif score>=80 :
    print("B")
elif score>=70 :
    print("C")
elif score>=60 :
    print("D")
else:
    print("E")
'''

#pratice5
#输入一个正整数判断是不是素数
#使用for in循环，素数指的是只能被1和自身整除的大于1的整数
'''
number = int(input("请输入一个正整数："))
is_prime = True
for x in (2,number**0.5):
    if number % x == 0:
        is_prime=False
        break
if is_prime and number!=1:
    print ("%d是素数"%number)
else:
    print("%d不是素数"%number)
'''
#pratice6
#打印三角形图案
'''
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()
'''

#practice7
#水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    hig = num // 100
    if num == hig**3 + mid**3 + low**3:
        print(num)
'''
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
'''

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')