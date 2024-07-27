from googletrans import Translator

def translate_text(text, src='ta', dest='en'):
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

if __name__ == "__main__":
    translated = translate_text("எப்படி இருக்கிறீர்கள்?", src='ta', dest='en')
    print(f"Translated text: {translated}")
