lst = [2,3,1,4]

sorted(lst) #funkce
lst.sort() # metoda

x = 42
print(x.__class__)

x = 42
print(type(x)) # calss int

y = "Hello"
print(type(y)) # class string

z = [1, 2, 3]
print(type(z)) # class list

x = 42
print(dir(x))
print(dir(type(x)))

x = 42
print(x.__class__)
print(x.__class__.__name__)


class Range: 
    def __init__(self, a: int,b: int|None = None, step:int|None = None):
        self.step = 1 if step is None else step 
        if not self.step: raise ValueError('wrong step')

        self.val = 0 if b is None else a
        self.end = a if b is None else b 

    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        if self.step < 0:
            if self.val <= self.end:
                raise StopIteration
            else:
                if self.end <= self.val:
                    raise StopIteration
            
            val = self.val
            self.val += self.stop 

            return val

for i in Range(14): print(i, end=' ')
print()
for i in Range(0,14): print(i, end=' ')
print()