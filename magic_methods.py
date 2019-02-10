# Before: you should either put the assignment __metaclass__ = type at the top of your modules

class FooBar:
    def __init__(self):
        self.somevar = 42

f = FooBar()
print f.somevar
