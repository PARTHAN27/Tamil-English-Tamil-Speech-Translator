from gtts import gTTS
import os

def synthesize_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    os.system("start output.mp3")

if __name__ == "__main__":
    synthesize_speech("Hello, how are you?", language='en')
