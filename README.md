# Intro
This project contains methods to test integration with Office365 and Gmail emails.

# Setup
Install python and dependencies.

Fill .env file with
```sh
OFFICE_CLIENT_ID="..."
OFFICE_CLIENT_SECRET="..."
OFFICE_TENANT_ID="..."
OFFICE_MAILBOX="..."
OFFICE_SEND_TO="..."
GMAIL_EMAIL="..."
```

Run main.py
```sh
fastapi dev main.py --port 8000
```

Go to (http://127.0.0.1:8000/docs)

Choose one of the methods and click "execute"

# Office 365

https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth#use-client-credentials-grant-flow-to-authenticate-smtp-imap-and-pop-connections

Connection is done on client side with OAuth2 client credentials grant flow.
In this case client id and client secret of Application are used and there is no user.

Project contains simple example for Graph API and Exchange protocols using https://github.com/O365/python-o365 library.

# Gmail
with OAuth2 user authorization code flow - user needs to make a consent.
Done and tested according to https://developers.google.com/gmail/api/quickstart/python with my personal gmail account.

Credentials should be downloaded from gmail and stored in *gmail-web-credentials.json* file.