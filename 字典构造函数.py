def mul(a,b):
    print(a*b)

def add(a,b):
    print(a+b)

def sum(a,b):
    print(a-b)

A={}
A['0']=add
A['1']=sum
A['2']=mul
a=int(input())
b=int(input())
c=input()
A[c](a,b)
