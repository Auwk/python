import itertools
a=[1,2,3,4,3]
b=[6,8,9]
c=[10,11]
d=0
for i in itertools.chain(a,b,c):    #chain使用演示
    print(i)
print('chain end')

for i in itertools.cycle(a):        #cycle使用演示
    print(i)
    d+=i
    if d>=40:                       #因为cycle为无限循环所以加一个条件使其停止
        break
 
