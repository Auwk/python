class init:
    def __init__(self,b=0,a=0,c=1):
        self.a=a
        self.b=b
        self.c=c

A=init()

def __range__(*f):
    y=0
    A.a=0
    A.c=1
    for i in f:
        y+=1
    if y==3:
        A.a=f[0]
        A.b=f[1]
        A.c=f[2]

    elif y==2:
        A.b=f[1]
        A.a=f[0]
        
    elif y==1:
        A.b=f[0]
        
    elif y==0:
        raise TypeError ("range expected 1 arguments, got 0")
        
    else:
        raise TypeError ("range expected at most 3 arguments, got %d"%y)
    if A.c>0:
        yield A.a
        while A.a<A.b:
            A.a += A.c
            if A.a<A.b:
                yield A.a
    else:
        yield A.a
        while A.a>A.b:
            A.a += A.c
            if A.a>A.b:
                yield A.a
        


for i in __range__(5):              #仅单个参数时调用
    print(i)
print()

for i in __range__(0,5,1):          #三个参数时调用
    print(i)
print()

for i in __range__(0,5):            #两个个参数时调用
    print(i)
print()

for i in __range__(5,0,-1):            #两个个参数时调用
    print(i)
print()

for i in __range__(1,2,3,4,5):      #参数过多时调用
    print(i)
print()

for i in __range__():               #无参数时调用
    print(i)
    
    

        

    
