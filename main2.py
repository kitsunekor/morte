from smtplib import SMTP

address_to_test = "ricardo.preira@exceltic.com"

try:
    with SMTP('gmail-smtp-in.l.google.com') as smtp:
        host_exists = True
        smtp.helo() # send the HELO command
        smtp.mail('ricardo.pereira@exceltic.com') # send the MAIL command
        resp = smtp.rcpt(address_to_test)
        if resp[0] == 250: # check the status code
            deliverable = True
        elif resp[0] == 550:
            deliverable = False
        else:
            print(resp[0])
except smtplib.SMTPServerDisconnected as err:
    print("SMTP connection error")

print(deliverable)

nbdl
