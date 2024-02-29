from pydantic import BaseModel

class Broker(BaseModel):
    id :str = ""
    provider :str = "alpaca"
    api_key :str = "******"
    api_secret :str = "***********"

class Owner(BaseModel):

    username :str = "username"
    surname :str = "surname"
    id :str = "00000001"
    brokers: Broker

