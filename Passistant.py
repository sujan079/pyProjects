# make sure that you install the pyaudio and speech recognition package 
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)#changing the voice to female voice
def talk(txt):
    engine.say(txt)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk("playing "+song)
        talk("playing")
        pywhatkit.playonyt(song)#plays the song form the youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        #formatting the time
        talk('Current time is'+time)
        print(time)
    elif 'who is' in command:
        main_word = command.replace('who is','')
        info = wikipedia.summary(main_word,1) #getting three line of the info form the wikipedia
        print(info)
        talk(info)
    elif 'what is' in command:
        main_word = command.replace('what is', '')
        info = wikipedia.summary(main_word, 1)  # getting three line of the info form the wikipedia
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry ,I am already occupied')
    elif 'are you single' in command:
        talk('I can\'t be in relation with anyone except your wifi')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'quit the program' in command:
        talk('goodbye')
    else:
        talk('Please say the command again')


while True:
    run_alexa()


