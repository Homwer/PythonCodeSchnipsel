### Abfrage; wie viele ungelesene Mails liegen im Postfach

import imaplib
mail = imaplib.IMAP4_SSL('alphard.uberspace.de')
mail.login('philipp@codingworld.io', 'PASSWORT')
mail.list()
mail.select("inbox")
data = mail.search(None, 'UNSEEN')


unreadmails = len(str(data[1]).split())
if str(data[1]) == "['']":
	unreadmails = 0
	
print unreadmails
