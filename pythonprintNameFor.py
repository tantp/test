# coding=gbk
StrArray = ["̸̩Ƽ", "³��", "������", "��־��"]  # �����б�����ʹ��append()׷��ֵ��delɾ���б��ֵ�ȣ����Ըı��б��е�ֵ
for i in range(len(StrArray)):
    #	print(StrArray[i])�����б�ֵ֮�任����ʾ
    print(StrArray[i], end=" ")
#	print(StrArray[i],end="") �����б�ֵ֮���޿ո���ʾ
print()  # ���ڻ��У�����հף�print()Ĭ�ϻ���
StrArray1 = ('tantp', 'luli', 'zhaoxiangli', 'mazhicheng', '̸ĳ')  # ����Ԫ�飬Ԫ�鲻�ܸı�Ԫ���е�ֵ
for j in range(len(StrArray1)):
    print(StrArray1[j])
# ע������������ѯ���Ƿ�����������������������˳��󣬴�ӡ�����������
nameArray = []
a = 1
while a == 1:
    name = input('������������')
    nameArray.append(name)
    continue_firm = input("��������'y',�˳��������:")  # ѯ���Ƿ�������룺�������ֵ���ڶ����ֵ�����������
    if (continue_firm == 'y'):
        a = 1
    else:
        a = 0
        print("�˳�����")
for i in range(len(nameArray)):
    print(nameArray[i], end=' \n')