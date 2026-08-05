from gpiozero import Button
from time import time, sleep
from datetime import datetime
import csv


class sleepChecker:
    def __init__(self, pin, log_path='sleep_log.csv', debounce_s=0.5):
        self.pin = pin
        self.log_path = log_path
        self.debounce_s = debounce_s
        self._last_time = 0
        self.is_sleeping = False

        try:
            # Button uses internal pull-up; press should connect pin to GND
            self.btn = Button(self.pin, pull_up=True, bounce_time=self.debounce_s)
            self.btn.when_pressed = self._handle_press
        except Exception as e:
            raise RuntimeError(f'gpiozero Button の初期化に失敗しました: {e}')

    def _handle_press(self):
        now = time()
        if now - self._last_time < self.debounce_s:
            return
        self._last_time = now

        if not self.is_sleeping:
            self.is_sleeping = True
            self.record_event('入眠')
        else:
            self.is_sleeping = False
            self.record_event('起床')

    def record_event(self, event):
        ts = datetime.now().isoformat()
        try:
            with open(self.log_path, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([ts, event])
        except Exception:
            # Avoid raising in callback context
            pass

    def cb_setSleep(self, channel=None):
        # Compatibility wrapper
        self.record_event('入眠')

    def cb_getSleep(self, channel=None):
        # Compatibility wrapper
        self.record_event('起床')

    def close(self):
        try:
            if hasattr(self, 'btn') and self.btn:
                self.btn.when_pressed = None
                self.btn.close()
        except Exception:
            pass


if __name__ == '__main__':
    sc = sleepChecker(pin=17)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        sc.close()
