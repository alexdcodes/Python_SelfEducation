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

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
    "October",
    "November",
]

years = [
    "1979",
    "1980",
    "1981",
    "1982",
    "1983",
    "1984",
    "1985",
    "1986",
    "1987",
    "1988",
    "1989",
    "1990",
    "1991",
    "1992",
    "1993",
    "1994",
    "1995",
    "1996",
    "1997",
]

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

print "\n\nContinue to domain names\n\n"
# Now to Split up a URL in the form of http://www.something.com

url = raw_input("Please enter the URL: ")
domain = url[11:-4]

# Continue the Split

raw_input("\nPress <enter> to end application")
