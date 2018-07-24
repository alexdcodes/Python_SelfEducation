# Just a simple application to do some calculations for me
# pings google.
# open source i guess i mean edit it as you please

from datetime import datetime
import os

# Message of the day and other quick settings

motd = "Welcome to My Number Calculator Application"
version = "0.1_alpha_build"
dir_path = os.path.dirname(os.path.realpath(__file__))
date = datetime.now()
print(motd, version)
print("\n Today's Date: %s/%s/%s" % (date.year, date.month, date.day), "| Successful Launch: %s:%s:%s" % (date.hour, date.minute, date.second))
print("\n")

#   Ping websites and make sure we have internet connection


def ping_network():
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)  # lets do some checking
    if response == 0:
        pingcheck = "\nNetwork Online"
    else:
        pingcheck = "\nNetwork Offline"

    return pingcheck


#   Enter your username and does name or what ever , to try validation


def account(username):
    while True:
        user_validation = input(username)
        if user_validation.isspace() or user_validation == "":	    # Validation
            print("That is not a valid username")
            continue
        else:
            return user_validation
        break

#   Makes it so the user has to enter a number


def input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("This is not a number")
            continue
        else:
            return user_input
        break

# Message and display the information back to the user


def message_calculations():
    if updated_number < number or updated_number == number:
        return "\nWtf..\nyou entered in the wrong number in the wrong location, or no new info got sent.."
    else:
        lolcount = updated_number - number
    print("\n [", user, "Information Statistics ]")
    print("\n> New Message Count: ", lolcount)
# displaying the lolCount number as a string


# Logging will go here  - We are outputting to log.txt


def create_log():
    file = open("log.txt", "a")
    file.write(user + " Data Log:")
    file.write("\t sent:\t" + str(log_text) + " ate apples    || Date: " + str(date))
    file.write("\n ---- \n")
    file.close()


user = account("> Enter your name: ")

# I might remove this later just for fun right now.

user_log = []
user_log.insert(0, user)

updated_number = input_number("> How many apples did you buy?: ")
number = input_number("> How many apples did you eat?: ")
log_text = updated_number - number

print(message_calculations())

print("\n>> Results will be stored in log.txt [in the application directory] " + dir_path)
print("\n This is typically the default folder the .py file is being executed from.")

create_log()

# Ask the use if they want to upload information to a remote SQL Database.
# In future i want to add remote SQL support.

print("\n>> Do you want to upload this data to an remote Database? (Y/N)")

print("\n\nSorry no Remote Support added yet. \n Lets do a simple Ping Test")

pingstatus = ping_network()

print("\n-- Online Check Statistics --")

print(pingstatus)
