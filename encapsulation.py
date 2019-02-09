__metaclass__ = type # Make sure we get new style classes


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


foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()

