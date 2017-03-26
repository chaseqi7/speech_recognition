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
    print("Set minimum energy threshold to {}".format(r.energy_threshold))

    while keepGoing:
        word=WORDS[random.randrange(0,len(WORDS))]
        b = raw_input("-------------------------------Start? y/n---------------------------------------")
        if b=="y":
            print("Say "+word+"!")
            with m as source: audio = r.listen(source)
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
        else:
            keepGoing=False
            break
except KeyboardInterrupt:
    pass
