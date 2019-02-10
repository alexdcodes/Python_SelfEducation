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
        Initalize the arthmetic sequence.

        start - the first value in the sequence
        step - the difference between two adjacent values
        changed - a dictionary of values that has been modified by the user
       """
    self.start = start
    self.step = step
    self.changed = {}


def __getitem__(self, key):
    """
    Get an item from the arithmetic sequence.
    """
    checkIndex(key)

    try: return self.changed[key]            # modified
    except KeyError:                         # otherwise.....
        return self.start + key*self.step    # calculate the value
