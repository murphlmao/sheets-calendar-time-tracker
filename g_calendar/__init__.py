from __future__ import print_function

import datetime
import os.path
import requests


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SECRETS = "./secrets/"
CLIENT_SECRET = SECRETS + "credentials.json"

creds = None
service = None

try:
    if os.path.exists('token.json'): # created when auth flow finishes for the first time
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)
        
except BaseException as error:
    print('An error occurred: %s' % error)
    raise