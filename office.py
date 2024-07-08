from O365 import Account, MSOffice365Protocol, MSGraphProtocol
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger('email-logger')
logging.basicConfig(level=logging.INFO)

load_dotenv()

client_id = os.getenv('OFFICE_CLIENT_ID')
client_secret = os.getenv('OFFICE_CLIENT_SECRET')
tenant_id = os.getenv('OFFICE_TENANT_ID')

mailbox_email = os.getenv('OFFICE_MAILBOX')
send_to = os.getenv('OFFICE_SEND_TO')

def send_o365_graph():
    credentials = (client_id, client_secret)

    account = Account(credentials, auth_flow_type = 'credentials', tenant_id=tenant_id, protocol=MSGraphProtocol())
    if account.authenticate():
        mailbox = account.mailbox(mailbox_email)
        m = mailbox.new_message()
        m.to.add(send_to)
        m.subject = 'Testing Jedox Email! (Graph API)'
        m.body = "Hello! Looks like email works with Graph API, great stuff! :)"
        m.send()
    else:
        print('not Authenticated!')


def send_o365_exchange():
    credentials = (client_id, client_secret)

    scopes = ["https://outlook.office365.com/.default"]

    account = Account(credentials, auth_flow_type = 'credentials', tenant_id=tenant_id, protocol=MSOffice365Protocol())
    if account.authenticate(scopes=scopes):
        mailbox = account.mailbox(mailbox_email) 
        m = mailbox.new_message()
        m.to.add(send_to)
        m.subject = 'Testing Jedox Email! (Exchange API)'
        m.body = "Hello! Looks like email works with Outlook Exchange API, cool stuff! :)"

        m.send()
    else:
        print('not Authenticated!')
