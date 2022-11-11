import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # or os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Ben French'
email['to'] = 'bfrenchy13@gmail.com'
email['subject'] = 'FROM ME TO ME'
email.set_content(html.substitute({'name':'Benny Boy'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('benfrenchtestemail@gmail.com', 'pfojggiouizpnccg')
	smtp.send_message(email)
	print('all good')