
import threading
import time
import serial



def sendInst():
    #send preamble
    string =  chr(int('00001100',2))
    s.write(bytes(string, 'utf-8'))
     

  
# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    with serial.Serial ('COM2',9600,parity=serial.PARITY_NONE,bytesize=8,stopbits=2, timeout=10) as s:
        sendInst()
