import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account

import base64
from email.message import EmailMessage

import os
from dotenv import load_dotenv

gmail_email = os.getenv('GMAIL_EMAIL')

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.send"]

def get_service_credentials(): 
  return service_account.Credentials.from_service_account_file('gmail-service-credentials.json', scopes=SCOPES)

def get_user_credentials():
  creds = None

  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "gmail-web-credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

def send_gmail_email(creds):
 
  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    
    message = EmailMessage()

    message["To"] = gmail_email
    message["From"] = gmail_email
    message["Subject"] = "Testing Jedox Email! (Gmail)"

    message.set_content("Hello! Looks like gmail email works with, nice! :)")

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )

  except HttpError as error:
    print(f"An error occurred: {error}")

def send_gmail_service_email():
  send_gmail_email(get_service_credentials())

def send_gmail_user_email():
  send_gmail_email(get_user_credentials())
