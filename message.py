from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC075adaa4b2d8bfe45df129dcdb65b932"
# Your Auth Token from twilio.com/console
auth_token  = "520cd80cd7982562e562698b47b4a7a3"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886932133221", 
    from_="+19035641275",
    body="Hello from Python!")

print(message.sid)