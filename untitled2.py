from tkinter import *
import speech_recognition as sr

root = Tk()
root.geometry("500x500")
root.title("Speech Recognition")
root.configure(background = "light grey")

def r_audio():
    speech_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognizer.listen(source)
        voice_data = ''
        
        try:
            voice_data = speech_recognizer.recognize_google(audio, language = 'en-in')
        except sr.UnknownValueError:
            print('Could you please repeat what you said? Thank you!')
        
    
    
    print(voice_data)
    
r_audio()
root.mainloop()