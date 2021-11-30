class Point:
    def __init__(self,x,y):
        if isinstance(x,int) and isinstance(y,int):
            self.x=x
            self.y=y
        else:
            print('Invalid values')

    def __str__(self):
        return f'Point ({self.x},{self.y})'
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Point(self.x-other.x,self.y-other.y)

    def __eq__(self, other):
        return isinstance(other,Point) and self.x==other.x and self.y==other.y
    def __hash__(self):
        return hash((self.x,self.y))
    def __len__(self):
        return self.x-self.y
    def __bool__(self):
        return self.x>0 and self.y>0
p=Point(15,17)
print(hash(p))
c=Point(10,17)
print(c)