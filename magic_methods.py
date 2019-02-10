# Before: you should either put the assignment __metaclass__ = type at the top of your modules

__metaclass__ = type


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


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError


f = FooBar()
b = Bird()
sb = BarkDog()
print sb.sing()
print f.somevar
print b.eat()
print b.eat()
