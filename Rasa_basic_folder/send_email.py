from __future__ import print_function

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#pip install --upgrade google-api-python-client
#pip install --upgrade oauth2client
def initialize_app(config):
	return email(config)


class email:
	def __init__(self, config):
		self.user_key = config["user_key"]



	# create a message
	def CreateMessage(self, sender, to, subject, message_text):
		"""Create a message for an email.

		Args:
		sender: Email address of the sender.
		to: Email address of the receiver.
		subject: The subject of the email message.
		message_text: The text of the email message.

		Returns:
		An object containing a base64 encoded email object.
		"""
		message = MIMEMultipart()
		message['to'] = to
		message['from'] = sender
		message['subject'] = subject
		#return {'raw': base64.b64encode(message.as_string())}

		#The body and the attachments for the mail
		message.attach(MIMEText(message_text, 'plain'))

		#Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		sender_address = sender
		sender_pass = 'admin!23456'
		receiver_address = to
		text = message.as_string()
		session.login(sender_address, sender_pass) #login with mail_id and password
		session.sendmail(sender_address, receiver_address, text)
		session.quit()

		return {'raw': message.as_string()}



	def main():
		# Shows basic usage of the Gmail API.
		# Send a mail using gmail API

		credentials = get_credentials()
		http = credentials.authorize(httplib2.Http())
		service = discovery.build('gmail', 'v1', http=http)

		msg_body = "test message"

		message = CreateMessage("hsatam@gmail.com", "hsatam@gmail.com", "Test Message Subject", msg_body)

		SendMessage(service, "me", message)

	if __name__ == '__main__':
		main()
