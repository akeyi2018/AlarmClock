import pigpio
from time import sleep

class sleepChecker:

    def __init__(self, pin):
	self.pin = pin
	pi = pigpio.pi() 
	pi.set_mode(self.pin, pigpio.OUTPUT) 
	pi.write(self.pin, 1)
        sleep(1.0)
	pi.write(self.pin, 0)

#         GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_UP)
# 	GPIO.add_event_detect(pin, GPIO.RISING, bouncetime=1000)
#         GPIO.add_event_callback(pin, cb_setSleep)

    def cb_setSleep(self, channel):

        #Set Timer For Wake Up
        pass

    def cb_getSleep(self,channel):
        pass
