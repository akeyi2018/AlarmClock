import datetime
import time

class AlarmTimer:
    
    def __init__(self, tm):

        #Get Now
        self.dt_now = datetime.datetime.now()
        
        if dt_now.hour > 0 and dt_now.hour <= tm[0]:
            #Set Time
            tmp = dt_now
        else:
            #Plus One day
            tmp = dt_now + datetime.timedelta(days=1)
            
        self.AlarmTime = datetime.datetime(tmp.year, tmp.month, tmp.day, tm[0], tm[1], 0, 0)
        print(self.AlarmTime)

    def RunAlarmTimer(self):
        
        while True:
            if datetime.datetime.now() > self.AlarmTime:
                print("Alem!!!")
                break
            else:
                time.sleep(1)


if __name__ == "__main__":        

    #Set Hour and minites
    tm = [7,30]

    #Set Alarm
    wt = AlarmTimer(tm)
    #Run Alarm
    wt.RunAlarmTimer()
