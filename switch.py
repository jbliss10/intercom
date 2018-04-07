import time # so we can use "sleep" to wait between actions
import RPi.GPIO as io # import the GPIO library we just installed but call it "io"
import requests
## set GPIO mode to BCM
## this takes GPIO number instead of pin number
io.setmode(io.BCM)
 
## enter the number of whatever GPIO pin you're using


io.setmode(io.BCM)      
io.setup(12, io.IN, pull_up_down=io.PUD_UP )  

io.setmode(io.BCM)       
io.setup(27, io.IN, pull_up_down=io.PUD_UP )

io.setmode(io.BCM)       
io.setup(22, io.IN, pull_up_down=io.PUD_UP )

def familyroom(channel):  
     if io.input(12):     
         res = requests.get('http://10.0.0.147:5005/office/join/family room')
         print "join family room"  
     else:                  
         res = requests.get('http://10.0.0.147:5005/office/leave/family room')
         print "leave family room"
    
def kitchen(channel):  
     if io.input(27):      
         res = requests.get('http://10.0.0.147:5005/office/join/family room')
         print "join kitchen"  
     else:                  
         res = requests.get('http://10.0.0.147:5005/office/leave/family room')
         print "leave kitchen"
         
def kitchen(channel):  
     if io.input(22):      
         res = requests.get('http://10.0.0.147:5005/office/join/living room')
         print "join living room"  
     else:                  
         res = requests.get('http://10.0.0.147:5005/office/leave/living room')
         print "leave living room"

io.add_event_detect(12, io.BOTH, callback=familyroom, bouncetime=500)
io.add_event_detect(27, io.BOTH, callback=kitchen, bouncetime=500)
io.add_event_detect(22, io.BOTH, callback=kitchen, bouncetime=500)

#while True:
try: 
    time.sleep(30)

finally:
    io.cleanup()