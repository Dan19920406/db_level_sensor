import serial, time
import requests

internalUrl = "internal api"
externalUrl = "external api"
deviceName = "device name"
#if value change > 10% will send data to api
def refresh_value(new, last=0):
    if last == 0:
        last = new
    else:
        if abs(new-last) > last*0.1:
            print(f'Bigger than 10% : {new}')
            data = {"Name":deviceName,"Value":new}
            try:
                r = requests.post(internalUrl, json=data, timeout=1.5)
            except:
                r = requests.post(externalUrl, json=data, timeout=1.5)
            print(f'Sent : {r.json()}')
        else:
            print(f'Smaller than 10% : {new}')
            new = last
    return new, last

#read serial port from serial_port.in
port = ''
with open("serial_port.in", 'r') as f:
    port = f.readlines()[0].replace('\n','')
ser = serial.Serial(port, 9600)     #init serial port
time.sleep(0.5)
ser.flushInput()    #clear input TS
new, last = refresh_value(int(str(ser.readline()).split('DB:')[1].replace('\\r\\n\'',''))/10)
data = {"Name":deviceName,"Value":new}
try:
    r = requests.post(internalUrl, json=data, timeout=1.5)
except:
    r = requests.post(externalUrl, json=data, timeout=1.5)
print(f'Sent : {r.json()}')

#Start monitor the db level
while True:
    ser.flushInput()
    try:
        new = int(str(ser.readline()).split('DB:')[1].replace('\\r\\n\'',''))/10
        last, void = refresh_value(new,last)
    except:
        print("Failed")
    time.sleep(5)

ser.close()
