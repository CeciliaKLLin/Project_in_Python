import smtplib

from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar to os.path

html = Template(Path('index.html').read_text()) #
email = EmailMessage()
email['from'] = '' # who send the email
email['to'] = '' # who receive the email(the email address)
email['subject'] = '' # the subject of the email

email.set_content('') # the content of the email e.g. html, text, images

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # part of the portocol
    smtp.starttls() # an encryption mechanism, we want to connect securely to the server.
    smtp.login('', '') # your email, your password
    smtp.send_message(email) # the above email we have created
    print('all done!')


