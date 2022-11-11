from twilio.rest import Client

account_sid = 'my given ID'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
	from_='+1my_phone'
	body='Hello, this is an automated message.'
	to='+1your_phone')

print(messge.sid)