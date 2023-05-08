from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class DevicesPayload(BaseModel):
    pushToken:str

class LogsPayload(BaseModel):
    logs:List[str]


app = FastAPI()

@app.post('/apple-pass/v1/devices/{device_library_identifier}/registrations/{pass_type_identifier}/{serial_number}/')
async def register(device_library_identifier:str,pass_type_identifier:str,serial_number:str,payload:DevicesPayload):
    print("identifier",device_library_identifier)
    print("pushToken ",payload.pushToken)
    return {'device_library_identifier': device_library_identifier, 'pass_type_identifier': pass_type_identifier, "serial_number": serial_number}


@app.get('/apple-pass/v1/devices/{device_library_identifier}/registrations/{pass_type_identifier}/')
async def getSerialNumber(device_library_identifier:str,pass_type_identifier:str):
    print("serial number")
    return {"serial_number":"this is serial number"}


@app.post('/apple-pass/v1/log/')
async def logs(payload:LogsPayload):
    print("logs",payload.logs)
    return {'data': 'awesome'}