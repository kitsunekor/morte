import re
import smtplib
import dns.resolver

# Address used for SMTP MAIL FROM command  

# Simple Regex for syntax checking
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

# Email address to verify
#inputAddress = input('Please enter the emailAddress to verify:')
#addressToVerify = str(inputAddress)

addressToVerify = 'ricardo.pereira@exceltic.com'

# Syntax check
match = re.match(regex, addressToVerify)
if match == None:
	print('Bad Syntax')
	raise ValueError('Bad Syntax')

# Get domain for DNS lookup
splitAddress = addressToVerify.split('@')
domain = str(splitAddress[1])
print('Domain:', domain)

# MX record lookup
records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)


# SMTP lib setup (use debug level for full output)
port = 25

fromAddress = 'victor.salgado@exceltic.com'
server = smtplib.SMTP("mail.exceltic.com",port)
server.starttls()
server.login("victor.salgado@exceltic.com","Pagm25dp+5")

server.set_debuglevel(7)

# SMTP Conversation
server.connect(mxRecord)
server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
server.mail(fromAddress)
code, message = server.rcpt(str(addressToVerify))
server.quit()

#print(code)
#print(message)

# Assume SMTP response 250 is success
if code == 250:
	print('Success')
else:
	print('Bad')