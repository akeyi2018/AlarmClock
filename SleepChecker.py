import RPi.GPIO as GPIO

class sleepChecker:

    def __init__(self, pin):

	self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_UP)
	GPIO.add_event_detect(pin, GPIO.RISING, bouncetime=1000)
        GPIO.add_event_callback(pin, cb_setSleep)

    def cb_setSleep(self, channel):

        #Set Timer For Wake Up
        pass

    def cb_getSleep(self,channel):
        pass
