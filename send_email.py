import smtplib
sender_mail = 'sender@mydomain.com'
receivers_mail = ['reciever@mydomaim.com']
message = """Well this is just an exaple
of an email script for eduaction purposes 
"""%(sender_mail,receivers_mail)
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender_mail, receivers_mail, message)
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")