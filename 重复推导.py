a=[{'a':1,'b':3,'c':3}
,{'a':3,'b':3,'c':8}
,{'a':2,'c':4,'m':6,'r':4},{'a':3,'b':2,'c':7,'o':5}
,{'a':7,'c':2,'m':7,'r':4}

]
'''f=[]
f.append(a[0])
for i in range(0,5,1):
    f.append([a[j] for j in range(i,5,1) if f[i].keys() != a[j].keys()])    
print(f)

'''
f=[]
k=0
for i in range(4,-1,-1):
    o =len(f)
    print(len(f))
    f.append([a[j]  for j in range(i-1,-1,-1) if a[i].keys() == a[j].keys() ])
    print(len(f))
    for y in range(i-1,-1,-1):
        if f[o]==[] and a[i].keys() == a[y].keys():
            f.remove([])
            k=1
            
    else:
        if k==0:
            f[o]=a[i]
print(f)
'''
k=5
f = a
for i in range(0,k,1):
    ([f.remove(a[i+1]) for j in f if a[i+1].keys() == j.keys()])
    k = len(a)
print(f)
'''
