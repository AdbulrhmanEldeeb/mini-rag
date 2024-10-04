from fastapi import FastAPI
from routes import base 
from dotenv import load_dotenv 
load_dotenv('.env')
app=FastAPI() 

from routes import data 


app.include_router(base.base_router)
app.include_router(data.data_router)

