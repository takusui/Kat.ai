import speech_recognition as sr
import pyttsx

speech = pyttsx.init('sapi5')


def talk(text):
    speech.say(text)
    speech.runAndWait()

recognize = sr.Recognizer()

def listen():
    r = True
    while r == True:
        with sr.Microphone() as source:
            recognize.adjust_for_ambient_noise(source)      # sets the energy treshold automatically
            audio = recognize.listen(source)

        try:
            recog = recognize.recognize_sphinx(audio)
            # print is used for debugging, change it to apply this
            # function in other programs.
            print recog
            r = False

        except sr.UnknownValueError:
            print("I didn't quite get that.")
            talk("I didn't quite get that.")
            r = True

        except sr.RequestError as e:
            print("Recog Error; {0}".format(e))
            r = False
            
        return recog

listen()
