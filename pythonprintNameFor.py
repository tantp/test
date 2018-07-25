# coding=gbk
StrArray = ["谈泰萍", "鲁俐", "赵香丽", "马志成"]  # 定义列表，可以使用append()追加值，del删除列表的值等；可以改变列表中的值
for i in range(len(StrArray)):
    #	print(StrArray[i])各个列表值之间换行显示
    print(StrArray[i], end=" ")
#	print(StrArray[i],end="") 各个列表值之间无空格显示
print()  # 用于换行，输出空白；print()默认换行
StrArray1 = ('tantp', 'luli', 'zhaoxiangli', 'mazhicheng', '谈某')  # 定义元组，元组不能改变元组中的值
for j in range(len(StrArray1)):
    print(StrArray1[j])
# 注释输入姓名，询问是否继续输入姓名，姓名输入退出后，打印出输入的姓名
nameArray = []
a = 1
while a == 1:
    name = input('请输入姓名：')
    nameArray.append(name)
    continue_firm = input("继续输入'y',退出按任意键:")  # 询问是否继续输入：如输入的值等于定义的值，则继续输入
    if (continue_firm == 'y'):
        a = 1
    else:
        a = 0
        print("退出输入")
for i in range(len(nameArray)):
    print(nameArray[i], end=' \n')