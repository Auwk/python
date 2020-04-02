def wow(fun):
    def js(*args,**kwargs):
        print('start...')
        fun(*args,**kwargs)
        print('end.')
    return js

@wow
def hi():
    print('wbnmsl')

hi()
        
