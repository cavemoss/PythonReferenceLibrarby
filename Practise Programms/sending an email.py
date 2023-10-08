#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#sending an email

import smtplib

sender ='alexshu1812@gmail.com'
receiver ='alexshu1812@gmail.com'
password ='141008igor'
subject ='Py email'
body ='an email'

message =   f'''    From: DOG{sender}
                    To:{receiver}
                    Sunject:{subject}\n
                    {body}
            '''

server =smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    server.login(sender, password)
    print('loged in')
    server.sendmail(sender,receiver,message)
    print('is has been sent')
except smtplib.SMTPAuthenticationError:
    print('unable to sign in')