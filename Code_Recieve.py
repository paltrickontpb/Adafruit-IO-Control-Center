from Adafruit_IO import Client
import os, time

KEY = 'ADAFRUIT-IO-KEY'

pyclient = Client(KEY)

code = 'xyz'

while 1:
    prencode = pyclient.receive('data')
    ncode=format(prencode.value)

    if (str(ncode)==str(code)):
        print ("No Updates")        
    else:
        code = str(ncode)
        print("Code Updated from cloud")

    time.sleep(10)
