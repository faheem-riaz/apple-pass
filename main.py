from time import time
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post('/apple-pass/v1/devices/{device_library_identifier}/registrations/{pass_type_identifier}/{serial_number}/')
async def hello(device_library_identifier:str,pass_type_identifier:str,serial_number:str):
    print(device_library_identifier)
    return {'device_library_identifier': device_library_identifier, 'pass_type_identifier': pass_type_identifier, "serial_number": serial_number}

@app.post('/apple-pass/v1/log/')
async def log():
    print("logs")
    return {'data': 'awesome'}