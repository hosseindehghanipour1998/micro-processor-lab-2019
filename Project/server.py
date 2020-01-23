import serial
import time
import struct

def getData():
    
    data = -1
    connected = False
    try:
        time.sleep(.5)
        header = s.read()
        print("Header : "  + str(ord(header)))
        header = ord(header)
        if (header == 170):
            connected = True
            print( "Connected ? -> " + str(connected) )
        if ( connected ):
            time.sleep(.5)
            inst = s.read()
            print("Instruction: " + str(ord(inst)))
            time.sleep(.5)
            lengthtemp = s.read()
            length = ord(lengthtemp)
            length1 = length
            while ( length1 > 0):
                time.sleep(.5)
                s2 = s.read()
                data = ( data * 256) + ord(s2)
                length1 = length1 - 1
            print ("Data : " + str(data) )
            time.sleep(.5)
            footer = s.read()
            x = ord(footer)
            print("Footer : " + str(x) )
    except:
        print("No Data received")
    return data
   
     
def sendData(pwmSpeedPercentage , instructionCode):
    datasent = ""
    
    #Send Header
    ''' = str(int('10101010',2))'''
    y = struct.pack("B",170)
    s.write(y)
    datasent += str(y) + "|"
    time.sleep(.5)
    #Send Instruction Type
    if ( instructionCode == 33 ):
        y = struct.pack("B",33)
        s.write(y)
        datasent += str(y)+ "|"
        time.sleep(.5)
    elif( instructionCode == 64 ):
        y = struct.pack("B",64)
        s.write(y)
        datasent += str(y)+ "|"
        time.sleep(.5)
    #Length Of 1
    y = struct.pack("B",1)
    s.write(y)
    datasent += str(y) + "|"
    time.sleep(.5)
    #Send Data 
    y = struct.pack("B",pwmSpeedPercentage)
    s.write(y)
    datasent += str(y) + "|"
    time.sleep(.5)
    #Send Footer
    y = struct.pack("B",255)
    s.write(y)    
    datasent += str(y) + "|"
    print("Sent Data : " + datasent )


def proceed():
    while(True):
        
                
            time.sleep(5)
            sendData(60,32)
            time.sleep(3)
            temperature = getData()
            pwm = 0 
            if ( temperature < 10 ):
                pwm = 30
            elif ( temperature >= 10 and temperature < 15 ):
                pwm = 60
            elif ( temperature >= 15 ):
                pwm = 90
            sendData(pwm , 64);
            print("============================")
            
        
            print("no Data Received")
    
if __name__ == "__main__":
    with serial.Serial ('COM2',9600,parity=serial.PARITY_NONE,bytesize=8,stopbits=2, timeout=10) as s:
        proceed()   
        #sendData(0,33)
