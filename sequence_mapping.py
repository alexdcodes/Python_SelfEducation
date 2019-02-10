def checkIndex(key):
    """
    IS the given key an accetable index?

    To not be acceptable, the key should be a non-negative integer.
     If it is not an integer, a type Error is raised; if it is negative, an IndexError is raised
     (since the sequence is of infinite length)
    """
    if not isinstance(key, (int, long)): raise TypeError
    if key<0: raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence.

        start - the first value in the sequence
        step - the difference between two adjacent values
        changed - a dictionary of values that has been modified by the user
       """


def __getitem__(self, key):
    """
    Get an item from the arithmetic sequence.
    """
    checkIndex(key)

    try: return self.changed[key]            # modified
    except KeyError:                         # otherwise.....
        return self.start + key*self.step    # calculate the value


def __setitem__(self, key, value):
    """
    Change an item in the arithmetic sequence
    """
    checkIndex(self)

    self.changed[key] = value               # store changed value


class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


cl = CounterList(range(10))
print cl
