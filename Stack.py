class Stack:
    def __init__(self):
        self.values=[]

    def push(self,item):
        self.values.append(item)
    def pop(self):
        if len(self.values)>0:
            a=self.values[len(self.values)-1]
            del self.values[len(self.values)-1]
            return a
        else:
            print( "Empty Stack")
    def top(self):
        if len(self.values)>0:
            return self.values[len(self.values)-1]
        else:
            print( "Empty Stack")
    def  is_empty(self):
        return False if len(self.values)>0 else True

    def size(self):
        return (len(self.values))

