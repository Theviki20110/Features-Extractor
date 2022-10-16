import smtplib
from random import randint, randbytes
import sys


#domain must be passed as: @gmail.com
domain = sys.argv[2]

sender = sys.argv[1] + domain
receiver = sys.argv[3]

header = """From: """+ sender +"""
To: """ + receiver


mailsubject = randbytes(randint(50, 400))

subject = "Subject: " + str(mailsubject) + '\n'

mailobject = randbytes(randint(100, 4000))

object = '\nBody: ' + str(mailobject)

messaggio = header + subject + object 
try:
    smtpObj = smtplib.SMTP(sys.argv[2])
    smtpObj.sendmail(sender, receiver, messaggio)
    print('OK')
except smtplib.SMTPException:
    print('ERROR')