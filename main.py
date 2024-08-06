from fastapi import FastAPI

import office as office_utils
import gmail as gmail

app = FastAPI()

@app.get("/microsoft/graph")
def root():
    office_utils.send_o365_graph()
    return {"message": "Graph email sent"}

@app.get("/microsoft/exchange")
def root():
    office_utils.send_o365_exchange()
    return {"message": "Exchange email sent"}

@app.get("/gmail/service")
def root():
    gmail.send_gmail_service_email()
    return {"message": "Gmail service email sent"}

@app.get("/gmail/user")
def root():
    gmail.send_gmail_user_email()
    return {"message": "Gmail user email sent"}