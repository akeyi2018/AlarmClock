class switchGpio:                                                                                                                                                                                                     def __init__(self, pin):

        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.RISING, bouncetime=1000)
        GPIO.add_event_callback(pin, cb_setSleepStatus)

    def cb_setSleepStatus(self, channel):

        #Set Timer For Wake Up
        Pass
