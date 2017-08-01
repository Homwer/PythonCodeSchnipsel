### Sends a request to the imap server for unread mails.

import imaplib

# Ask the user for their information
server = raw_input("Please enter your Imap Server: ")
email = raw_input("Please enter your Mailadress: ")
password = raw_input("Please enter your password: ")

# Enter your data here, and uncomment, unsafe but handy solution !
#server = "SERVER"
#email = "Mailadress"
#password = "PASSWORD"


mail = imaplib.IMAP4_SSL(server)
mail.login(email, password)
mail.list()
mail.select("inbox")
data = mail.search(None, 'UNSEEN')


unreadmails = len(str(data[1]).split())
if str(data[1]) == "['']":
	unreadmails = 0
	
print unreadmails
