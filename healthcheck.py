import requests
import time
import smtplib
import re
import datetime

EMAIL_ADDRESS = 'pchahal@ojolabs.com'
EMAIL_PASSWORD = 'zqdhnngvsamihsku'
CONTACTS = ['pchahal@ojolabs.com', 'database@wolfnet.com', 'daniel.engle@wolfnet.com', 'henry.liao@wolfnet.com', 'sam.hough@wolfnet.com', 'andrew.mikos@wolfnet.com', 'hliao@ojolabs.com', 'amikos@ojolabs.com']


count = 0
while True:
    r = requests.get('https://ca0b73.listingdetails.com/main/testSite', auth=('bigbad','wolf'), timeout=10)
    if r.status_code !=200:
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                subject ='WolfNet API is DOWN'
                body = 'Please kick API servers'
                msg = 'Subject: {}\n\n{}'.format(subject, body)

                smtp.sendmail(EMAIL_ADDRESS, CONTACTS, msg)
            print("Email sent successfully!")
            print("status_code not eq 200 error")
            print(datetime.datetime.now())
        except Exception as ex:
            print("Something went wrong", ex)
            print(datetime.datetime.now())

    else:
        #print(r.text)
        result = re.search('This site can’t be reached', r.text)
        if result:
            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                    subject = 'WolfNet API is DOWN'
                    body = 'Please kick API servers'
                    msg = 'Subject: {}\n\n{}'.format(subject, body)

                    smtp.sendmail(EMAIL_ADDRESS, CONTACTS, msg)
                print("Email sent successfully!")
                print("website timeout error error")
                print(datetime.datetime.now())
            except Exception as ex:
                print("Something went wrong", ex)
                print(datetime.datetime.now())
        else:
            count += 1
            print(r.status_code)
            print('iterration number: ' + str(count))
            print(datetime.datetime.now())

    time.sleep(900)

else:
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = 'WolfNet API is DOWN'
            body = 'Please kick API servers'
            msg = 'Subject: {}\n\n{}'.format(subject, body)

            smtp.sendmail(EMAIL_ADDRESS, CONTACTS, msg)
        print("Email sent successfully!")
        print("while loop condition fail error")
        print(datetime.datetime.now())
    except Exception as ex:
        print("Something went wrong", ex)
        print(datetime.datetime.now())