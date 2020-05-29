#!/usr/bin/env python
#coding:utf-8
days=int(input("Enter days: ")) ##!/usr/bin/python
months=days//30
day=days%30
print("Months={}  Days={}".format(months,day))
print("Months={}  Days={}".format(*divmod(days,30)))
#divmod(num1,num2)  num1 he num2 xingchuquzhengshu ,diergezhi num1 he num2 xiangchuqudeyushu,yong*chaifengzhegeyuanzu,deidaolianggezhi.
print('1<2:{}'.format(1<2))
print('3<34:{}'.format(3>34))
print('23==45:{}'.format(23==45))
print('34!32:{}'.format(34!=32) )

a=[23,45,1,-3344,43624356,234]
print(a)
a.append(45)
print('a.append(45)之后a={}'.format(a))
a.insert(0,1) #在索引0位置增加1
print('a.insert(0,1)之后,a={}'.format(a))
a.insert(2,22)
print('a.insert(2,22)之后，a={}'.format(a))
print('a.count(23)23在a中出现的次数={}'.format(a.count(23)))
a.remove(234)
print('a.remove(234)之后a={}'.format(a))
a.reverse() #反转a列表
print('a.reverse()之后a={}'.format(a))
b=[45,56,90]
print('b={}'.format(b))
a.extend(b) #添加b的元素而不是b本身
print('a.extend(b)之后a={}'.format(a))
a.sort()
print('a.sort()之后a={}'.format(a))
del a[-1]
print('del a[-1]之后a={}'.format(a))
print('aaaaaa')