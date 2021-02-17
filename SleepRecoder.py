import os

class sleepRecoder:

    def __init__(self, path):
        self.path = path
        self.config_json_file = os.path.join(self.path, 'config.json')

    def recordSleepTime(self):
        #record sleep time
        pass

    def recordWakeupTime(self):
        #record wakeup time
        pass
        
