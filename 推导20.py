a=[int(input("输入整数\n")) for i in range(0,20,1)]
b=[v for v in a if v>0]
c=[d for d in a if d<0]
print(b)
print(c)
