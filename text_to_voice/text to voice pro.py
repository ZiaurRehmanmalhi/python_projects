import pyttsx3


def speech(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')[1]
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 1.5)
    engine.say(x)
    engine.runAndWait()


speech("i am program")
