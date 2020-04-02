class book:
    def __init__(self,name='python 从入门到入土'):
        self.name=name

    def __add__(self,obj):
        return self.name + ' + ' + obj.name

    def __len__(self):
        return len(self.name)

if __name__=='__main__':
    A=book()
    B=book('我打死不入土！！')
    print('len(A)',len(A))
    print('len(B)',len(B))
    print(A+B)
    print(B+A)
