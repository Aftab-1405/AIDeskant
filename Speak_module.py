import pyttsx3
from Database import speak_is_on
from Database import *

"""-------------------------THIS IS SPEAK FUNCTION------------------------------"""

# Take output retuned after processing and spoken it by assistant.


def speak(o):
    if speak_is_on():
        rate = 100
        tts = pyttsx3.init("sapi5")
        voices = tts.getProperty('voices')
        tts.setProperty('voice', voices[0].id)
        tts.setProperty("rate", rate + 50)
        tts.say(o)
        tts.runAndWait()


"""-------------------------THIS IS A CHANGE VOICE FUNCTION-----------------------'"""
# This function uses two other function of database module for its operation is such a way that if voice will be changed then after new name of the assistant will be updated in databse.


def change_voice():

    from Output_module import output
    from Input_module import take_input
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')

    # Get new assistant name from user
    output("Please enter the name of voice you would like to use:")
    output("Options are as follows:\nNumber 1: rake\nNumber 2: inertia")
    new_voice = take_input()

    if new_voice == 'rake':
        tts.setProperty('voice', voices[0].id)
        update_name("Rake")
        update_voice(voices[0].id)
        (speak("Sure Sir, I have changed my voice. How does this sound?"))
        return "Voice is updated."

    elif new_voice == 'inertia':
        tts.setProperty('voice', voices[1].id)
        update_name("inertia")
        update_voice(voices[1].id)
        speak("Sure Sir, I have changed my voice. How does this sound?")
        return "Voice is updated."

    else:
        return "Sorry Sir, I don't have that voice. Please try again."


    # Initialize TTS engine with default voice
tts = set_default_voice()

"""----------------------------------------------------------------------------------"""
