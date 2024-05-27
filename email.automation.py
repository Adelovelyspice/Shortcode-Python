import smtplib
#creating funtions
def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('senderemail','password')
    server.sendmail('senderemail', 'mary-adeola@gmail.com','testing email automation!')
    server.close()

    sendEmail()
  