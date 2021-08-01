from os.path import dirname, join as pjoin

from scipy.io import wavfile
import time
import scipy.io



wav_fname = pjoin("../music", 'example1.wav')


samplerate, data = wavfile.read(wav_fname)
length = data.shape[0] / samplerate

print(samplerate)
#display the data in realtime

samplesPerSecond = 10
currentTime = 0

while currentTime < length:

    #translate time to current idx
    idx = (int)(currentTime * samplerate)

    print(str(data[idx,0]) + " at " + str(currentTime) + " s")
    time.sleep(1/samplesPerSecond)
    currentTime += (1/samplesPerSecond)


