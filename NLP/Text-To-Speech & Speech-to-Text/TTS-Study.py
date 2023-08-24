from gtts import gTTS
from tempfile import TemporaryFile
import os
import time
import subprocess
import simpleaudio as sa #https://realpython.com/playing-and-recording-sound-python/

# Reference : https://www.youtube.com/watch?v=_Q8wtPCyMdo
x = "Selamat Sore. Saya Ani dari Toko Buku AniBooks. Ada yang bisa saya bantu?"
language = 'id' # di cmd gtts-cli --all
output = gTTS(text=x,lang=language) # Cari biar lebih cepet
print(output)

# Ganti suara bisa gak? Gabisa
# https://stackoverflow.com/questions/37600197/custom-python-gtts-voice

output.save('belajar.mp3')
# os.system("start belajar.mp3")

# import keyboard #Using module keyboard
# while True:  #making a loop
#     try:  #used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed(' '): #if key space is pressed.You can also use right,left,up,down and others like a,b,c,etc.
#             print('You Pressed A Key!')
#             break #finishing the loop
#     except:
#         pass


import subprocess
PLAYERPATH = "C:\Program Files (x86)\K-Lite Codec Pack\Media Player Classic\mplayerc.exe"
x = subprocess.call([PLAYERPATH, 'belajar.mp3'], creationflags=subprocess.CREATE_NEW_CONSOLE)
print('tesss----')

# subprocess.Popen('belajar.mp3', creationflags=subprocess.CREATE_NEW_CONSOLE)

# import librosa
# import wave
# import soundfile as sf
# x,_ = librosa.load('belajar.mp3', sr=16000)
# sf.write('tmp.wav', x, 16000)
# wave.open('tmp.wav','r')


# import sounddevice as sd
# import soundfile as sf
#
# filename = 'belajar.mp3'
# # Extract data and sampling rate from file
# data, fs = sf.read(filename, dtype='float32')
# sd.play(data, fs)
# status = sd.wait()  # Wait until file is done playing


# f = TemporaryFile()
# output.write_to_fp(f)
# with open('belajar.mp3', 'wb') as f:
#     output.write_to_fp(f)
# output.write_to_fp('belajar.wav')

from time import sleep
# import pyglet
#
# music = pyglet.media.load('belajar.mp3', streaming=False)
# music.play()
# print(music.duration)
# sleep(20) #prevent from killing

# x = subprocess.call(['ffmpeg', '-i', 'belajar.mp3', 'belajar.mp3'])
# filename = 'belajar.mp3'
# wave_obj = sa.WaveObject.from_wave_file('belajar.mp3')
# play_obj = wave_obj.play()
# play_obj.wait_done()  # Wait until sound has finished playing

# # https://stackoverflow.com/questions/260738/play-audio-with-python?rq=1
# https://stackoverflow.com/questions/49121947/how-to-play-a-sound-file-in-python-using-subprocess-without-stopping-the-program
# import subprocess
# subprocess.call(["afplay", "belajar.mp3"])

# from playsound import playsound
# playsound("file location\audio.p3")


# Pelajari
# https://github.com/nicknochnack/WatsonSTT/blob/master/Watson%20Speech%20to%20Text.ipynb
# ChatBot Indonesia
# https://www.youtube.com/watch?v=bOqcK8qTXkA
# Robot nya nanti aja pake NLP


