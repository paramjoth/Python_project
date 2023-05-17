
import os
import smtplib
from email.message import EmailMessage #need to import this lib for second method

EMAIL_ADDRESS = 'pchahal@ojolabs.com'
EMAIL_PASSWORD = 'zqdhnngvsamihsku'
CONTACTS = ['kaur.paramjoth@gmail.com', 'pchahal@ojolabs.com']

#first method
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#
#     subject ='Testing emails'
#     body = 'Did you receive the email?'
#
#     msg = f'Subject: {subject}\n\n{body}'
#
#     smtp.sendmail(EMAIL_ADDRESS, CONTACTS, msg)

#Second method, you can send attachments with second method

msg = EmailMessage()
msg['Subject'] = 'WolfNet API is DOWN'
msg['From'] = EMAIL_ADDRESS
msg['To'] = CONTACTS
msg.set_content('Please kick API servers')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)



