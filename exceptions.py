class MuffledCalculator:
    def __init__(self):
        pass

    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivsionError:
            if self.muffled:
                print "Division by zero is denied"
            else:
                raise


calculator = MuffledCalculator()
print calculator.calc('10/2')
