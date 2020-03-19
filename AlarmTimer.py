import datetime
import time
from SleepSchedule import schedule

class AlarmTimer:
    
    def __init__(self, tm, flag):
        
        #Force flag
        self.flag = flag
        
        #Get Now
        dt_now = datetime.datetime.now()
        
        if dt_now.hour > 0 and dt_now.hour <= tm[0]:
            #Set Time
            tmp = dt_now
        else:
            #Plus One day
            tmp = dt_now + datetime.timedelta(days=1)

        #Get Holiday Info
        if self.flag == 1:
            self.isOffWork = False
        else:
            self.isOffWork = schedule(tmp.date()).IsOffWork()
            
        self.AlarmTime = datetime.datetime(tmp.year, tmp.month, tmp.day, tm[0], tm[1], 0, 0)
    

    def RunAlarmTimer(self):

        if self.isOffWork:
            return 0

        #print("Alarm Set:", self.AlarmTime)
        
        while True:
            
            if datetime.datetime.now() > self.AlarmTime:
                print("Alem!!!")
                break
            else:
                time.sleep(1)


if __name__ == "__main__":        

    #Set Alarm
    wt = AlarmTimer([7,30],0)
    
    #Run Alarm
    wt.RunAlarmTimer()

