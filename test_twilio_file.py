#!/usr/bin/python2

from datetime import datetime
from datetime import time
from time import sleep
import json
import subprocess
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# -----------------------------------------------------------------------------
# USER INPUTS
ACCOUNT_SID = "account SID from .jay. account" # Your Account SID from www.twilio.com/console
AUTH_TOKEN  = "token from .jay. account"  # Your Auth Token from www.twilio.com/console
TO_NUMBER = "+ put my phone number starting with a 1 here after the plus with no space"
FROM_NUMBER = "+ phone number from the .jay. account"  # .jay. account

# -----------------------------------------------------------------------------

try:
    # Find these values at https://twilio.com/user/account
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message_body = "testing the Twilio"
    message = client.messages.create(
        to=TO_NUMBER,
        from_=FROM_NUMBER,
        body=message_body)

    print('test SMS sent')
except:
    print ('error sendingr SMS')
