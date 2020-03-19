import datetime
import vlc
import time
import RPi.GPIO as GPIO

class MusicPlayer:

    def __init__(self, musicPath):

        self.musicPathh = musicPath
        #prepare music
	self.player = vlc.MediaListPlayer()
	self.mediaList = vlc.MediaList([self.musicPath])
        self.player.set_media_list(self.mediaList)
        self.player.set_playback_mode(vlc.PlaybackMode.loop)

    def Play(self):
        pass

    def Stop(self):
        pass

    def GetMusic(self):
        pass

    def SetMusic(self):
        pass

class sleepRecoder:

    def __init__(self):
        self.recordFile = recordFile

    def recordSleepTime(self):
        #record sleep time
        pass

    def recordWakeupTime(self):
        #record wakeup time
        pass

class scadule:

    def __init__(self, requst):
        
        self.weekFlag = [1,1,1,1,1,0,0]
        self.holiday = []
        self.requst = requst
        
    def getScadule(self):

        #compare weekflag
        #compare holiday
        pass
        return True

class humanInfo:

    def __init__(self):

        self.age = [10,20,30,40,50,60,70,80]
        self.gender = ["Male","Femail", "other"]
        self.occupation = [""]        

    def getSleepingrism(self):
        pass
        return True

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
