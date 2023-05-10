from typing import List
from fastapi import FastAPI, Response
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import os

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
    current_time = datetime.utcnow()
    print("pass update since",passesUpdatedSince)
    if(passesUpdatedSince == None):
        print("Pass Updated since is not present")
    
    return {"lastUpdated":current_time,"serialNumbers":["E5982H-I2",]}


@app.get('/apple-pass/v1/passes/{pass_type_identifier}/{serial_number}')
async def getPasses(pass_type_identifier:str,serial_number:str):
    pass_path = get_pass_file_path()
    pass_data = read_pass_file(pass_path)  # replace with your pass data
    # Create the response
    response = Response(content=pass_data, media_type="application/vnd.apple.pkpass")
    response.headers["Last-Modified"] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    return response


@app.post('/apple-pass/v1/log')
async def logs(payload:LogsPayload):
    print("logs",payload.logs)
    return {'data': 'awesome'}


def read_pass_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    return content


def get_pass_file_path():
    static_folder = os.path.abspath('static')
    pass_file_path = os.path.join(static_folder, 'apperciTest2.pkpass')
    return pass_file_path