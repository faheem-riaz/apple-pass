from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DevicesPayload(BaseModel):
    pushToken:str

class LogsPayload(BaseModel):
    logs:List[str]


app = FastAPI()

@app.post('/apple-pass/v1/devices/{device_library_identifier}/registrations/{pass_type_identifier}/{serial_number}')
async def register(device_library_identifier:str,pass_type_identifier:str,serial_number:str,payload:DevicesPayload):
    print("identifier",device_library_identifier)
    print("pushToken ",payload.pushToken)
    return {'device_library_identifier': device_library_identifier, 'pass_type_identifier': pass_type_identifier, "serial_number": serial_number}



@app.get('/apple-pass/v1/devices/{device_library_identifier}/registrations/{pass_type_identifier}')
async def getSerialNumber(device_library_identifier:str,pass_type_identifier:str,passesUpdatedSince:Optional[str] = None):
    current_time = datetime.now()
    print("pass update since",current_time)
    
    return {"lastUpdated":current_time,"serialNumbers":["E5982H-I2",]}


@app.post('/apple-pass/v1/log')
async def logs(payload:LogsPayload):
    print("logs",payload.logs)
    return {'data': 'awesome'}