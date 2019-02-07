# Check a username and PIN Code

database = [
    ['albert', '1234'],
    ['dylan', '0001'],
    ['ralph', '0502'],
    ['jane', '0003']
]
database_two = [
    ['Bob', '1111'],
    ['Tom', '2222'],
    ['Kat', '3333'],
    ['Storm-Flies', '4444']
]

database.extend(database_two)

username = raw_input('Username: ')
pin = raw_input('PIN Code: ')

if [username, pin ] in database: print 'Access Granted!'
if [username, pin ] not in database: print "Denied"
