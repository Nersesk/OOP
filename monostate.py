class Mono:
    __attr={
        'state':True,
        'name':'X',

    }
    def __init__(self):
        self.__dict__=Mono.__attr

a=Mono()
print(a.__dict__)
b=Mono()
print(b.__dict__)
a.state=False
print(a.__dict__)
print(b.__dict__)
