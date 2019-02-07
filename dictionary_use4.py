names = [
    'John',
    'Bob',
    'Beth',
    'Cecil',
    'Dee-Dee',
    'Earl',
]

numbers = [
    '3000',
    '3001',
    '3002',
    '3003',
    '3004',
    '3005',
]

print numbers[names.index('Beth')]

# Using Dictionaries Instead

phonebook = {'Anna': '2002', 'Dee-Dee': '3004', 'Cecil': '3003'}

print phonebook['Anna']

# Simple Database

# A dictionary with zoo animal(s) as keys,
# each zoo animal(s) is represented as another dictionary
# with keys location and ID referring to
# their ID numbers

animals = {
 'Turtle': {
    'location': 'Zoo',
    'id': '0001'
},
 'Donkey': {
    'location': 'Zoo',
    'id': '0002'
},
 'Sloth': {
    'location': 'Zoo',
    'id': '0001'
}
}

# Descriptive labels for the location and id number

labels = {
    'location': 'Location',
    'id': 'Identification Number'
}

name = raw_input('Name: ')

# Are we looking for a phone number or an address?

request = raw_input('Animal (l) or ID (a)?')

# Use the correct key:

if request == 'l' : key = 'location'
if request == 'a' : key = 'id'

# Only print if valid key from dictionary

if name in animals: print "%s's %s is %s." % \
                          (name, labels[key], animals[name][key])