#!/usr/bin/env python3

from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=['https://mail.google.com/'])
credentials = credentials.with_subject('enp@itx.ru')

service = build('gmail', 'v1', credentials=credentials)

message = MIMEText('TEST MESSAGE')
message['to'] = 'enp@itx.ru'
message['from'] = 'enp@itx.ru'
message['subject'] = 'Test Message'
print(message)

message = (service.users().messages().send(userId='me', body={'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}).execute())
print(message)
