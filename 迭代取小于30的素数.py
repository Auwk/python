class dd():
    def __init__(self,x=1,max=30):
        self.x=x
        self.max=max

    def __iter__(self):
        return self
    def __next__(self):
        if self.x:
            self.x +=1
            if self.x < self.max:
                for i in range(2,self.x):
                    if self.x % i ==0:
                        return self.x
                    else :
                        continue
            else:
                raise StopIteration                  
        else:
            raise StopIteration
        

if __name__=='__main__':
    A=dd()
    print('小于三十的素数有')
    a=0
    for i in A:
        if i != None:
            a += 1
            if a == 11:
                print('')
            print(i,end=' ')
            
