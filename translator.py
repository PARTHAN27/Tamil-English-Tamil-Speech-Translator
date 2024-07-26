from googletrans import Translator
from gtts import gTTS
# Initialize the translator
translator = Translator()
# Translate text
text_to_translate = ""
translated_text = translator.translate(text_to_translate, src='en', dest='ta')
# Print the translated text
print(f"Original: {text_to_translate}")
print(f"Translated: {translated_text.text}")
tts = gTTS(text=translated_text.text, lang='en')
tts.save("test.mp3")