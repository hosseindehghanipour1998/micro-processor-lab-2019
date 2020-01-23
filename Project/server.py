import serial
import threading as th
import time


def getData():
    data = -1
    connected = False
    header = s.read()
    print("Header : "  + str(ord(header)))
    header = ord(header)
    if (header == 170):
        connected = True
        print( "Connected ? -> " + connected )
    if ( connected ):
        inst = s.read()
        print("Instruction: " + str(ord(inst)))
        lengthtemp = s.read()
        length = ord(lengthtemp)
        length1 = length
        while ( length1 > 0):
            s2 = s.read()
            data = ( data * 256) + ord(s2)
            length1 = length1 - 1
        print ("Data : " + str(data) )
        
        footer = s.read()
        x = ord(footer)
        print("Footer : " + str(x) )
    return data
   
     
def sendData(pwmSpeedPercentage , instructionCode):
    
    #Send Header
    s.write(chr(int('10101010',2)))
    
    #Send Instruction Type
    if ( instructionCode == 32 ):
        s.write(chr(int('00100000',2)))
    elif( instructionCode == 64 ):
        s.write(chr(int('01000000',2)))
    
    #Length Of 1
    s.write(chr(1))
    
    #Send Data 
    s.write(chr(int(pwmSpeedPercentage)))
    
    #Send Footer
    s.write(chr(int('11111111',2)))     
   
def proceed():
    while(True):
        time.sleep(5)
        sendData(60,32)
        temperature = getData()
        pwm = 0 
        if ( temperature < 10 ):
            pwm = 30
        elif ( temperature >= 10 and temperature < 15 ):
            pwm = 60
        elif ( temperature >= 15 ):
            pwm = 90
        sendData(pwm , 64);
        
    
    
# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop
def printer():
    
    print("hi")
    #th.Timer(5.0,printer).start()
    
if __name__ == "__main__":
    with serial.Serial ('COM2',9600,parity=serial.PARITY_NONE,bytesize=8,stopbits=2, timeout=10) as s:
        proceed()   
