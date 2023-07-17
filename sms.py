
from twilio.rest import Client

account_sid = 'AC8ca55bc3c1aef707469bd2f0becb8f58'
auth_token = '160bdc5e85ce5b8b7550101dc0110c15'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18662404660',
  body='Hi, this is the test msg from twillio',
  to='+19792292816'
)

print(message.sid)