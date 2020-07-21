#coding:utf-8
import wave
import struct
from scipy import fromstring,int16
import numpy as np
import math
import alsaaudio as alsa
import audioop
from gpiozero import LEDBarGraph
from multiprocessing import Process
from time import sleep

class Sound:

    def __init__(self, wavefile, Low_sound, High_sound):

        self.wavefile = wavefile
        #LEDの設定
        #self.graph = LEDBarGraph(21,20,16,5,6,13,19,26,pwm=True)
        self.graph = LEDBarGraph(26,19,13,6,5,16,20,21,pwm=True)
        #SOUNDの設定
        self.chunk = 2048
        self.Low_sound_level= Low_sound
        self.High_sound_level= High_sound
        self.out = alsa.PCM(alsa.PCM_PLAYBACK, alsa.PCM_NORMAL,'hw:1,0')
        self.out.setrate(44100)
        self.out.setformat(alsa.PCM_FORMAT_S16_LE)
        self.out.setchannels(2)
        self.out.setperiodsize(320)
        self.stream = wave.open(self.wavefile,"r")

    def calculate_levels(self, data):
        fmt ="%dH" % (len(data)/2)
        data = struct.unpack(fmt,data)
        return np.array(data, dtype='h')

    def play(self):
        #ファイルのパラメータを取得する
        param = self.stream.getparams()
        totalCount = int(param[3]/param[2])*100
        for _ in range(totalCount):
            data = self.stream.readframes(self.chunk)
            if not data:
                break
            self.out.write(data)
            res = self.calculate_levels(data)
            re = float(max(audioop.max(res,2),1))
            re2 = (max(re - self.Low_sound_level, 0))/(self.High_sound_level - self.Low_sound_level)
            re2 = min(re2, 1)

            self.drawg(re2)

    def drawg(self, re):
        self.graph.value = re

def wrapper(wavFile):
    snd = Sound(wavFile, 2000, 22000)
    snd.play()

def SetInitialLED(wavFile):
    snd = Sound(wavFile, 10000, 22000)
    snd.drawg(0)

if __name__== "__main__":

    wavFile = "/mnt/samba/peliz.wav"
    thread = Process(target=wrapper, args=(wavFile,))
    thread2 = Process(target=SetInitialLED, args=(wavFile,))
    print("thread1 start")
    thread.start()
    print("SLEEP 10 ")
    for cnt in range(10):
        print(cnt)
        sleep(1)
    print("thread2 start:")
