import smtplib
from email.mime.text import MIMEText

# E-Mail-Verbindung herstellen
smtp_server = 'smtp.1und1.de'
smtp_port = 587
username = 'tv@pro-vreden.de'
password = '#'

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

# E-Mail-Inhalt erstellen
sender = 'tv@pro-vreden.de'
recipient = 'kerstin@pro-vreden.de'
subject = 'Test Email'
message = 'This is a test email from Raspberry with Pyhton'

msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# E-Mail senden
server.sendmail(sender, [recipient], msg.as_string())

# Verbindung beenden
server.quit()
