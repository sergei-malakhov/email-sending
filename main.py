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


@app.get("/gmail/oauth2")
def root():
    gmail.send_gmail_email()
    return {"message": "Exchange email sent"}