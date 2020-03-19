import jpholiday

class schedule:

    def __init__(self, reqDay):
        
        self.dt = reqDay
        self.isHoliday = jpholiday.is_holiday(self.dt)
        self.holidayName = jpholiday.is_holiday_name(self.dt)
        
    def IsOffWork(self):
        if self.isHoliday:
            return True
        elif self.dt.weekday() >= 5:
            return True
        else:
            return False      
        
if __name__ == "__main__": 
    pass
