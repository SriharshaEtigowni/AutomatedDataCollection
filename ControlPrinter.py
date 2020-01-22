import time
import os
import shutil
import serial

Xval__ = -1
Yval__ = 0
Zval__ = 1.3

s = serial.Serial("COM4",250000)
print 'Opening Serial Port'
s.write("\r\n\r\n") # Hit enter a few times to wake the Printrbot
time.sleep(2)   # Wait for Printrbot to initialize
s.flushInput()  # Flush startup text in serial input

def removeComment(string):
	if (string.find(';')==-1):
		return string
	else:
		return string[:string.index(';')]

def initsend():
    print 'Sending gcode'
    sendcode("G28")
    sendcode("M400")
	
	
def sendcode(l):
    global s
    l = removeComment(l)
    l = l.strip() # Strip all EOL characters for streaming
    if  (l.isspace()==False and len(l)>0) :
        print 'Sending: ' + l
        s.write(l + '\n') # Send g-code block
        grbl_out = s.readline() # Wait for response with carriage return
        print ' : ' + grbl_out.strip()
		
def getval():
    global Xval__
    global Yval__
    global Zval__

    if Xval__ < 280:
        Xval__ = Xval__ + 1
    elif Yval__ < 280:
        Xval__ = 0
        Yval__ = Yval__ + 1
    else:
        Xval__ = 0
        Yval__ = 0
        Zval__ = Zval__ + 0.1

    strin = "G1 X" + str(Xval__) + " Y" + str(Yval__)  + " Z" + str(Zval__)

    return strin

def sendandcapture__():
    global Xval__
    global Yval__
    global Zval__
    xya = getval()
    sendcode(xya)
    sendcode("M400")
    if Xval__ == 0:
        time.sleep(15)
    else:
        time.sleep(0.3)
		
    if Zval__ >= 3:
        exit()

    
def main():
    initsend()
    while True:
        sendandcapture__()

if __name__ == '__main__':
    main()
