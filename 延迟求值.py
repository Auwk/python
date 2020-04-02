def bb(a,b):
    def mul():
        print(a+b)
    return mul
a=0
b=0
a=int(input())
b=int(input())
A=bb(a,b)
print('————我是延时线————')
A()
    
