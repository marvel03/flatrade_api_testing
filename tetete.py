from pythonAPI.api_helper import NorenApiPy

import logging
import pandas as pd

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
userid='FZ29502'
usersession ='89dd9e5f2b1f8179586c80cec9524cfa793eb6ba5a9c1baf437c33263ce2be88'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)
print("start")
print(ret)

# print(api.__susertoken)

scrip=api.searchscrip_1(exchange='NSE', searchtext='RELIANCE')
scrip_list=pd.DataFrame(scrip["values"])
print(scrip_list)
# print(scrip)