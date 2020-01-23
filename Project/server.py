
import serial

def getData():
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
        data = 0
        while ( length1 > 0):
            s2 = s.read()
            data = ( data * 256) + ord(s2)
            length1 = length1 - 1
        print ("Data : " + str(data) )
        
        footer = s.read()
        x = ord(footer)
        print("Footer : " + str(x) )
   
     
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
    
    
    


def sendInst():
    #send preamble
    string =  chr(int('00001100',2))
    s.write(bytes(string, 'utf-8'))
     

  
# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    with serial.Serial ('COM2',9600,parity=serial.PARITY_NONE,bytesize=8,stopbits=2, timeout=10) as s:
    
        getData()   
