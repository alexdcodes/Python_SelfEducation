from math import sqrt

print ("Hello world\n\n")
print sqrt(10)

name = raw_input("What is your name? ")
print "Hello,  " + name + "!"
print "\nPython Scripts for testing\n\n"
x = "Hello"
y = "World"

print (y, x)

temp = "42"
print "The temperature is " + temp

print '''\n THIS IS A JUST A TESTING APPLICATION FOR EDUCATION NOTHING MORE, .
.. EXAMPLE OF A VERY LONG STRING PROGRAM IN PYTHON'''


endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']

year = raw_input('Year:  ')
month = raw_input('Month (1-12): ')
day = raw_input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

# Remember to subtract 1 from month and day to get the correcet index

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print month_name + ' ' + ordinal + ', ' + year

raw_input("\nPress <enter> to end application")
