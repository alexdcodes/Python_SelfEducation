# Check a username and PIN Code

database = [
    ['albert', '1234'],
    ['dylan', '0001'],
    ['ralph', '0002'],
    ['jane', '0003']
]

username = raw_input('Username: ')
pin = raw_input('PIN Code: ')

if [username, pin ] in database: print 'Access Granted!'
if [username, pin ] not in database: print "Denied"