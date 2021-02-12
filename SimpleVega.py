import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('I am vega  an artificial intelligence at your service')
engine.say('How can i help you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'vega' in command:
                command = command.replace('vega', '')
                print(command)
    except:
        pass
    return command


def run_vega():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info_person = wikipedia.summary(person, 5)
        print(info_person)
        talk(info_person)
    elif 'what is' in command:
        things = command.replace('what is', '')
        info_thing = wikipedia.summary(things, 5)
        print(info_thing)
        talk(info_thing)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I am sorry. Can you repeat it again.')


run_vega()

