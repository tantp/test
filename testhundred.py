#!/usr/bin/env python2.7
number=int(input('Enter an integer:'))
if number<=100:
    print('You number is less than or eaual to 100')
else:
    print("Your number is greater than 100")

w=20
while w>1:
	print('w={}'.format(w))
	w-=1

amount=float(input("Enter amount: ")) #shurushue
inrate=float(input("Enter inrate rate:")) #shurulilv
period=int(input("Enter period:")) #shuruqixian
value=0
year=1
for year in range(period):
	value=amount+(amount*inrate)
	print("year {} Rs. {:.2f}".format(year,value)) #:{.2f},baoliuliangweixiaoshu
	amount=value
	year+=1