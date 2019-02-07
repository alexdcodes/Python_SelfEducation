x, y, z = 1, 2, 3

print x, y, z

name = raw_input("What is your name? ")
if name.endswith('Alex'):
    if name.startswith('Mr.'):
        print 'Hello Mr. Alex'
    elif name.startswith('Mrs.'):
        print 'Hello Mrs. Alex'
    else:
        print 'Hello, Alex'
else:
    print 'Hello, Stranger'


def enter_number():

    num = input("Enter a number: ")
    if num > 0:
        print 'The number is positive'
    elif num < 0:
        print 'The number is negative'
    else:
        print 'The number is zero'


enter_number()


def boolean_operators():

    number = input("Enter a number from 1 to 10: ")
    if number <= 10:
        if number >= 1:
            print 'Great!'
        else:
            print 'Wrong!'
    else:
        print 'Wrong!'


boolean_operators()


# Loop 1 - 100
def while_loop():

    x = 1
    while x <= 100:
        print x
        x += 1


while_loop()
