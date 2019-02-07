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