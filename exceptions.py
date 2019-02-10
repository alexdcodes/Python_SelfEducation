def describeanimal(animal):
    print 'Description of', animal['name']
    print 'Age:', animal['age']
    try:
        print 'Type of Animal: ', + animal['occupation']
    except KeyError: pass


class MuffledCalculator:
    def __init__(self):
        pass

    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivsionError:
            if self.muffled:
                print "Division by zero is illegal"
            else:
                raise


# Zen of Exceptions
calculator = MuffledCalculator()

print calculator.calc('10/2')
