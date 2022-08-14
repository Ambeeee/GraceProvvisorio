from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError              # pip install SpeechRecognition, pip install PyAudio
import pyttsx3                                                                                      # pip install pyttsx3
import os
from time import sleep


listener = Recognizer()                                                                             # ascolta
engine = pyttsx3.init()                                                                             # sintesi vocale
engine.setProperty('rate', 150)                                                                     # velocità
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class Engine:

    #INFOS
    def __init__(self, name, audio=1, times=[1,"y"]):
        self.name = name.lower()
        self.audio = audio
        self.times = times                                                                      # [t, i] >   t (times): int, i(infinite): y/n 
        
    def set_gender(self, gender):
        match gender:
            case 'FEMALE':
                self.engine.setProperty('voice', self.voices[0].id) 
            case 'MALE':
                self.engine.setProperty('voice', self.voices[1].id)

    #OUTPUT
    def say(self, content):
        if self.audio == 1:     engine.say(content)
        else:                   print(content)
    
    def report(self, content):
        if self.audio == 1:
            engine.say(content)
        print(content)

    def decor(content):
        decorator="-"
        for i in content:
            decorator += "-"
            final = f"""
                {decorator}
                {content.upper()}
                {decorator}
            """
        return final

    #INPUT
    def is_activated(self, content):
        command = content.split()
        for word in command:
            match word:
                case self.name:
                    for w in command:
                        if w == self.name:
                            pass
                        del command[0]
                        
                    print("Attivato!")
                    return " ".join(command)
                case _:
                    self.listen()
    
    def listen(self):
        self.content = ""
        if self.audio == 1:
            with Microphone() as source:
                print("ascolto...")
                listener.adjust_for_ambient_noise(source, duration=0.5)
                listener.pause_threshold = 1.0                                                     #secondi dopo fine frase
                listener.record(source, 1)
                voice = listener.listen(source)
                try:
                    self.content = listener.recognize_google(voice, language='it-IT').lower()
                except UnknownValueError:
                    self.report("Mi dispiace, non ho capito")
                except RequestError:
                    self.report("Mi dispiace, connessione Internet scarsa o assente")
        else:
            self.content = input("Di cosa hai bisogno? ")
        self.is_activated(self.content)

    def run(self):
        while self.times[0] > 0:
            self.listen()
            sleep(.5)
            if self.times[1] == "n":
                self.times[0] -= 1
                print(f"Utilizzi rimasti: {self.times[0]} ")






