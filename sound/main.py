from flask import Flask, render_template, request
from MultiPlaywave import Sound
from multiprocessing import Process
import glob

app = Flask(__name__)

def getmusicInfo():
    list = {}
    cnt = 0
    for file in glob.glob("/mnt/samba/*.wav"):
        list[cnt] = file
        cnt = cnt + 1
    return list

def wrap_play(filename):
    global led
    snd = Sound(filename, 10000, 30000)
    snd.play()

@app.route("/kill/<val>", methods=['POST'])
def stop_play(val):
    play.terminate()
    #app.logger.info("stop play")
    return render_template("index.html", selectedval = int(val), musiclink=getmusicInfo())

@app.route("/showfile", methods=['GET','POST'])
def main():

    wavFile= 0

    global play
    if request.method == 'POST':
        if request.form['bt'] =='PLAY':
            wavFile = str(request.form["musicfile"])
            #app.logger.info("wavFile: " + wavFile)
            musicFile = getmusicInfo()[int(wavFile)]
            #app.logger.info("selected: "+musicFile)
            play = Process(name="play", target=wrap_play, args=(musicFile, ))
            play.start()
            #app.logger.info("play start")
    return render_template("index.html", selectedval = int(wavFile),
                            musiclink=getmusicInfo())

if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0')
