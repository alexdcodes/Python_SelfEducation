# Before: you should either put the assignment __metaclass__ = type at the top of your modules


class FooBar:
    def __init__(self):
        self.somevar = 42


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print 'Aaah...'
            self.hungry = False
        else:
            print 'No, thanks!'


class BarkDog(Bird):
    def __init__(self):
        self.sound = 'Woof'

    def sing(self):
        print self.sound


f = FooBar()
b = Bird()
sb = BarkDog()
print sb.sing()
print f.somevar
print b.eat()
print b.eat()
