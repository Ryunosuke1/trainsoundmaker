
import numpy as np
import matplotlib.pyplot as plt
from os.path import dirname, join as pjoin

##import time
import scipy
from scipy.io.wavfile import write
import wave
import math
##from pydub import AudioSegment
import soundfile as sf
import pyrubberband as pyrb

##import nazo
from numpy import frombuffer
import click
import sys



##end2 = 0



##@click.command()
##@click.argument('ad', 'accelerationdeceleration', prompt="Acceleration and Deceleration(m/h/s)", help="Type acceleration and deceleration(m/h/s)")
##@click.argument('maxiumspeed', prompt="maxiumspeed", help="Type maxium speed")
##@click.argument('time', prompt="train running time", help="Type train running time")
##@click.argument('gearratio', prompt="gearratio(bigger smaller)")
##def trainsoundsound(accelerationdeceleration, maxiumspeed, time, gearratio):

    ##global end2
    ##global maxspee
    ##global acceleration
    ##global deceleration
    ##global g1
    ##global g2

    ##acceleration, deceleration = accelerationdeceleration
    ##maxspee = maxiumspeed
    ##end2 = time
    ##g1, g2 = gearratio
    ##trainsound()

    ##global g1
    ##global g2

   ## maxspee = request.form.get("maxiumspeed")
   ##acceleration = request.form.get("acceleration")

    ##deceleration = request.form.get("deceleration")
    ##g1 = request.form.get("biggearratio")
    ##g2 = request.form.get("smallgearratio")


end1 = 0
# 時間（秒）
##timestart = 0
##0 <= timestart <= end1
##timestart = time.time()
##end2 = 0
##end92 = end2 * 44100
##acceleration = None
##acceleration2 = acceleration / 3600
##brake = -3.5
##bnake = brake / 3600
##spee = 0
##spee2 = 0
##j = 0
##u = 0
##nanashi2 = 0
##end4 = 0
##end7 = 0
##end9 = 0
##diameter = 860
##diameter2 = diameter / 1000
##x = diameter2 * math.pi
# 人は死ぬ　いつか死ぬ
##g1 = 82
##g2 = 17
##y = g1 / g2
##nanashi = 0


def speedup():
    sound_path = 'sine.wav'
    ##s, rate = sf.read(sound_path)
    yy, sr = sf.read(file="sine.wav")
    y_stretch = pyrb.time_stretch(yy, sr, 44100)
    sf.write("sinesine.wav", y_stretch, sr, format='wav')


theendsoon = 0
##    global acceleration
##    global maxspee
##    global end2
##    global g1
##    global g2

#@click.command()
#@click.option('ad', 'accelerationdeceleration', default=[1.8, 3.5], prompt="Acceleration and Deceleration(m/h/s)", help="Type acceleration and deceleration(m/h/s)", multiple=True)
#@click.option('maxiumspeeddiameter',defaul prompt="maxiumspeed_diameter", help="Type maxium speed and wheel diameter", multiple=True)
#@click.option('time', prompt="train running time", help="Type train running time")
#@click.option('gearratio', prompt="gearratio(bigger smaller)",multiple=True)
acceleration = sys.argv[1]
deceleration = sys.argv[2]
maxiumspeeds = sys.argv[3]
diameter = sys.argv[4]   
time = sys.argv[5]
g1 = sys.argv[6]
g2 = sys.argv[7]

filelist = [None]

def trainsound(aa, bb, cc, dd, ee, ff, gg):
    ##global acceleration
    global acceleration2
    ##global deceleration
    global end2
    ##global diameter
    global bnake
    global endsoon
    global end92
    ##acceleration, deceleration = accelerationdeceleration
    ##maxspee, diameter = maxiumspeeddiameter
    end2 = ee
    ##g1, g2 = gearratio
    end92 = end2 * 44100
    acceleration2 = aa / 3600
    bnake = bb / 3600
    maxspee = cc * 1000 / 3600

    spee = 0
    spee2 = 0
    j = 0
    u = 0
    nanashi2 = 0
    end4 = 0
    end7 = 0
    end9 = 0
    diameter2 = dd / 1000
    x = diameter2 * math.pi
    y = ff / gg
    nanashi = 0
    endsoon = 0

    for end111 in range(end92):
        acceleration2 = acceleration / 3600
        end111 = + 1
        global end137
        end137 = end111 - 1
        end137= str(end111) + "a.wav"        ##end111 = (end92 - 1) /44100 + 1
        time3 = end92 - (maxspee / bnake) * 44100
        filelist.append(end137)
        time4 = end92 - time3
        time2 = (maxspee / (acceleration / 3600)) * 44100
        if end2 >= 79380000:
            break
        print('最高速度(km/h)', maxspee, '\n直径', diameter, '\n時速(km/h)',
              spee, '\n加速度(m/h/s)', acceleration, '経過時間', end111)
        if 0 <= end111 <= time2:
            spee = 0 + acceleration2 * end92 / 44100
        if time2 < end111 < time3:
            spee = spee2
        if time3 <= end111 < end1:
            spee = spee2 + (time4 * bnake)
            frequency = spee / x
            f = frequency * y * g2
            rate = 44410
            sec = 1.0
            hurehaba = 1.0
            ##phase = np.cumsum(2 * np.pi * f / rate * np.ones(int(rate * end2)))
            wave = np.arrange(0, sec, 1 / rate)  # -1.0 〜 1.0 の値のサイン波
            wave2 = hurehaba * np.sin(2 * np.pi * f * wave)
            plt.plot(wave, wave2)
            scipy.io.wavfile.write(end137,44100, wave2(np.int16))
    else:
        join_waves(filelist, "sinesine.wav")



    # wave = (wave * float(2 ** 15 - 1)).astype(np.int16)  # 値域を 16bit にする
    ##g = scipy.io.wavfile.write('sinesinesinesine' + str[end2] + 'a.wav', rate, wave)
    ##p = {}.setparams(nchannels = 1, sampwidth = 2, framerate = rate, nframes = rate, comptype = None, compname = "not compressed")
    end4 = end2
    nanashi13 = range(end7)
    ##exec('{} = None'.format(nanashi13))

    ##scipy.io.wavfile.write(end137, 44100, 44100, wave2(np.int16))
    endsoon = 1




def main():
    trainsound(acceleration, deceleration, maxiumspeeds, diameter, time, g1, g2)
    
# end main
    


def join_waves(inputs, output):
    
    try:
        fps = [wave.open(f, 'r') for f in inputs]
        fpw = wave.open(output, 'w')

        fpw.setnchannels(fps[0].getnchannels())
        fpw.setsampwidth(fps[0].getsampwidth())
        fpw.setframerate(fps[0].getframerate())

        for fp in fps:
            fpw.writeframes(fp.readframes(fp.getnframes()))
            fp.close()
        fpw.close()

    except wave.Error:
        pass

    except Exception:
        pass




if endsoon == 2:
    speedup()




##if __name__ == '__main__':

    ##inputs = [str(n) + '.wav' for n in range(end92)]
    ##output = 'sine.wav'
    ##endsoon = 2

    ##join_waves(inputs, output)
# if end2 == end7:
    ##l = range(3980000)
    ##h = AudioSegment.empty()

    # for nanashi in range(end7):
    ##v = h.append(AudioSegment.from_file(file=end137[nanashi]))
    # exec(v)
    # sound1 = AudioSegment.from_file('imput' + str(nanashi) +"a.mp3"))
# if nanashi >= end7:
    # for nanashi11 in h:
    ##nanashisound += nanashi11
    ##thend = 1
# if theendsoon == 1:
    ##sound = nanashisound.speedup(playback_speed = 44100)
##    sound.export("sound.wav", format = "wav")


# Footer
