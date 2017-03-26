import speech_recognition as sr
import random

r = sr.Recognizer()
m = sr.Microphone()
keepGoing=True
WORDS = "how,pick,random,word,from,long,list,apple,something,can,think,mike,banana,camera"
WORDS=WORDS.split(",")

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Please say something for setting up voice print")
    with m as source:
        audio = r.listen(source)
    with open("voice-print-base.wav", "wb") as f:
        f.write(audio.get_wav_data())

    print("Set minimum energy threshold to {}".format(r.energy_threshold))

    while keepGoing:
        word=WORDS[random.randrange(0,len(WORDS))]
        b = raw_input("-------------------------------Start? y/n---------------------------------------")
        if b=="y":
            print("Say "+word+"!")
            with m as source:
                audio = r.listen(source)
            with open("microphone-results.wav", "wb") as f:
                 f.write(audio.get_wav_data())
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = str(r.recognize_google(audio)).lower()
                print("You said: "+value)
                if value==word:
                    print("Speech Recgnition:PASS!")
                else:
                    print("Speech Recgnition:FAIL!")
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

            #do the speaker diarization here
        else:
            keepGoing=False
            break
except KeyboardInterrupt:
    pass
