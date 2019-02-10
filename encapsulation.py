__metaclass__ = type
# Make sure we get new style classes


class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name


class Class:
    def method(self):
        print 'I have a self!'

    def function():
        print "I dont.."


class Animal:
    sound = "Bark"

    def sing(self):
        print self.sound


# Lets add privacy so we cannot modify the property from the outside

# We will add two underscores to kinda show that this class should not be accessed, also attempt to hide it.

class Secretive:

    def __inaccessible(self):
        print "Hidden class just shown by underscores. Can still be accessed in python of course.."

    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()


class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1


class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter): # SPAMFilter is a subclass of Filter
    def init(self): # Overrides init methods from Filter superclass
        self.blocked = ['SPAM']


f = Filter()
f.init()
f.filter([1,2,3])
s = SPAMFilter()
isinstance(s, SPAMFilter)
s.init()
s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()

