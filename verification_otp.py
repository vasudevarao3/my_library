import random
from twilio.rest import Client
otp = random.randint(10000,99999)
number=input("Enter the mobile number:")
account_sid="AC88b93e3bda93cd8dc1b8abaef1731c7a"

auth_token='2f3e4380b66e31fd5b02fa9ec03db2fd'

client=Client(account_sid,auth_token)

msg=client.messages.create(
    body="your OTP is %s."%otp,
    from_="+16208378238",
    to="+91%s."%number
)