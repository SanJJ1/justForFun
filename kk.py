import numpy as np
import simpleaudio as sa
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.fft import fft

# calculate note frequencies
A = 440
scale = [A * 2 ** ((i - 48) / 12) for i in range(88)]
complete = [["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"][i % 12] + str(i // 12) for i in
            range(9, 97)]
notes = {}
for i in range(88):
    notes[complete[i]] = scale[i]
    notes[" rest "] = 0

# get timesteps for each sample , T is note duration in seconds

sample_rate = int(44.1 * 10 ** 3)
time = .18

t = np.linspace(0, time, int(time * sample_rate), False)

# mix audio together


# practice = np. linspace (0 , 1 , 20 , False )
# print ( practice )
# practice = np.sin( practice * 2 * math .pi)
# print ( practice *100)


# noteSequence = [" e4" , "d4" , "c4" , "d4" , "e4" , "e4" , "e4" , " rest " , "d4" , "d4" , "d4" , " rest " , "e4" , "g4" , "g4 "]
# noteSequence = [i for i in notes . keys ()]
noteSequence = ["d5", "c#5", "c5",
                "b4", " rest ", "g4", "d4", "d4", "g4",
                "b4", "b4", "g4", "d5", "d5", "b4",
                "g5", "f#5", "g5", "a5", "g5", "f#5",
                "g5", "g5", "d5", "b4", "b4", "g4",
                "f#4", "f#4", "e4", "f#4", "f#4", "g4",
                "a4", "a4", "b4", "c5", "b4", "a4",
                "d5", "d5", "c#5", "d5", "d5", "e5",
                "f#5", "f#5", "d5", "c5", "c5", "a4",
                "b4", " rest ", "g4", "d4", "d4", "g4",
                "b4", "b4", "g4", "d5", "d5", "b4",
                "g5", "f#5", "g5", "a5", "g5", "f#5",
                "g5", "g5", "d5", "b4", "b4", "g4",
                "b4", "c5", "d5", "g5", "g5", "d5",
                "c5", "c5", "a4", "f#4", "f#4", "g4",
                "a4", "a4", "g4", "g4", "g4", "f#4",
                "g4", "g4", "g4", "d5", "c#5", "c5",
                "b4", " rest ", "g4", "d4", "d4", "g4",
                "b4", "b4", "g4", "d5", "d5", "b4",
                "g5", "f#5", "g5", "a5", "g5", "f#5",
                "g5", "g5", "d5", "b4", "b4", "g4",
                "f#4", "f#4", "e4", "f#4", "f#4", "g4",
                "a4", "a4", "b4", "c5", "b4", "a4",
                "d5", "d5", "c#5", "d5", "d5", "e5",
                "f#5", "f#5", "d5", "c5", "c5", "a4",
                "b4", " rest ", "g4", "d4", "d4", "g4",
                "b4", "b4", "g4", "d5", "d5", "b4",
                "g5", "f#5", "g5", "a5", "g5", "f#5",
                "g5", "g5", "d5", "b4", "b4", "g4",
                "b4", "c5", "d5", "g5", "g5", "d5",
                "c5", "c5", "a4", "f#4", "f#4", "g4",
                "a4", "a4", "g4", "g4", "g4", "f#4",
                "g4", "g4", "g4"]
offset = 0
n = len(t)

audio = np.zeros((math.ceil(time * sample_rate * len(noteSequence)), 2))

for i in range(len(noteSequence)):
    audio[0 + offset: n + offset, 0] += np.sin(notes[noteSequence[i]] * t * 2 * math.pi)
    audio[0 + offset: n + offset, 1] += np.sin(notes[noteSequence[i]] * t * 2 * math.pi)
    offset = math.ceil(time * sample_rate * (i + 1) * .05)

c = np.sin(notes["c4"] * t * 2 * math.pi)
e = np.sin(notes["e4"] * t * 2 * math.pi)
g = np.sin(notes["g4"] * t * 2 * math.pi)

# cChord = sum(np.sin( notes [i] * t * 2 * math .pi) for i in noteSequence )
cChord = c + e + g
# plt. plot (np. linspace (0 , time , tim
# e * sample_rate * audioLength -1 , False ), audio [0: -1 , 0])
plt.plot(t, c, color="r")
plt.plot(t, e, color="blue")
plt.plot(t, g, color="green")
plt.plot(t, cChord, color="black")
ft = fft(cChord)
n = len(ft) // 16
xScale = 500
# plt. plot (t[0:n] * xScale , np.abs(ft [0:n]))
plt.ylim([-3, 3])
plt.xlim([0, .1])

red_patch = mpatches.Patch(color='r', label='C4')
blue_patch = mpatches.Patch(color='b', label='E4')
green_patch = mpatches.Patch(color='g', label='G4')
black_patch = mpatches.Patch(color='black', label='The Chord')

plt.legend(handles=[red_patch, blue_patch, green_patch, black_patch])
plt.show()
# normalize to 16 - bit range
audio = audio * 32767 / np.max(np.abs(audio))
# convert to 16 - bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

# play_buffer () parameters :
# audio_data : object with audio data ( must support the buffer interface )
# num_channels (int): the number of audio channels
# bytes_per_sample (int): the number of bytes per single - channel sample
# sample_rate (int): the sample rate in Hz

# wait for playback to finish before exiting
play_obj.wait_done()
