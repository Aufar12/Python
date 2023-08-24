import speech_recognition as sr

# Reference : https://www.youtube.com/watch?v=GluSLXFGfJ8&t=1s
# https://codeloop.org/python-speech-recognition-with-google-speech/

def main():
    r = sr.Recognizer()

    x = sr.Microphone()
    y = sr.AudioFile('recorded.mp3')

    with x as source:  # Ganti x sm y nya
        r.adjust_for_ambient_noise(source)
        print("Jawab Pertanyaannya.")

        audio = r.listen(source) #phrase_time_limit=5
        jawaban = r.recognize_google(audio, language='id')

        try:
            print('Anda Menjawab : ' + jawaban)
        except Exception as e:
            jawaban = 'Error'
            print(e)

        with open("recorded.mp3", "wb") as f:
            f.write(audio.get_wav_data())

main()


# PElajari
# https://github.com/nicknochnack/WatsonSTT/blob/master/Watson%20Speech%20to%20Text.ipynb
# ChatBot Indonesia
# https://www.youtube.com/watch?v=bOqcK8qTXkA
