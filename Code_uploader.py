from Adafruit_IO import Client

KEY = 'ADAFRUIT-IO-KEY'

pyclient = Client(KEY)

code = raw_input('Enter the Code : ')
print("Input Code : "+str(code))

pyclient.send('data', code)
print("Code updated in cloud")

