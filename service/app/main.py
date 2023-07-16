from locale import currency
from datetime import datetime as dt
from fastapi import FastAPI, Response
from http import HTTPStatus
import time
#import configparser
from fastapi.logger import logger

#config = configparser.ConfigParser()
#config.read("etc/config.ini")

app = FastAPI()

def createResponseBody(start, args = None):
    ret = {
        "timestamp": dt.now(),  
    }

    if args is not None:
        for i in args:
            ret[i] = args[i]

    ret["duration"] = round(time.time() - start, 3)    

    return ret

@app.get("/ping")
async def pong(response: Response):
    start = time.time()
    response.status_code = HTTPStatus.OK

    return createResponseBody(start, { 
        "pong": dt.now()
        })
