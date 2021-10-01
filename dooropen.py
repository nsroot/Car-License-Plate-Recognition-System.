import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
          # set GPIO24 as an output   

def main():
    GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
    GPIO.setup(13, GPIO.OUT) 
    GPIO.output(13,GPIO.HIGH)         # set GPIO24 to 1/GPIO.HIGH/True  
    sleep(0.5)                 # wait half a second  
    if GPIO.input(13):  
        print ("LED just about to switch off" ) 
    GPIO.output(13, GPIO.LOW)         # set GPIO24 to 0/GPIO.LOW/False  
    sleep(0.5)                 # wait half a second  
    if not GPIO.input(13):  
        print ("LED just about to switch on")
        GPIO.cleanup()
