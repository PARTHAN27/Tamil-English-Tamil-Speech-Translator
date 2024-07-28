import speech_recognition as sr

def recognize_speech(language='en-US'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=language)
            print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognize_speech()
