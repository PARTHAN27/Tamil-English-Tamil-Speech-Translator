#recognise and transcribe speech
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.AudioFile("C:/Users/Parthan/Downloads/audio.wav") as source:
    audio_data = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio_data)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
print(text) 
