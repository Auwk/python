class pz:
    def __init__(self,name='pz'):
        self.name=name

    def quack(self):
        print('我嘴臭，我光荣')

class duck:
    def __init__(self,name='duck'):
        self.name=name

    def quack(self):
        print('嘎嘎嘎嘎')

class dog:
    def __init__(self,name='iroman'):
        self.name=name
        print('I m iron man')

def duck_demo(obj):
    obj.quack()

pz=pz()
duck=duck()
dog=dog()
duck_demo(pz)
duck_demo(duck)
duck_demo(dog)
        
