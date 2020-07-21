import subprocess
import sys
from multiprocessing import Process
from time import sleep

class mpxplayer:

    def __init__(self):

        self.musicfile = sys.argv[1]
        self.cmd = "mplayer -ao alsa:device=hw=1.0 -novideo -shuffle -playlist " + self.musicfile

    def run(self):
        proc =subprocess.Popen(self.cmd.split(), shell=False)


def wrapper(obj):
    p = mpxplayer()
    p.run()

if __name__ == "__main__":

    thread = Process(target=wrapper, args=("",))
    thread.start()
