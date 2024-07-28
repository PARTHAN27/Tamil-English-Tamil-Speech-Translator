from speech_recognition.recognizer import recognize_speech
from translation.translator import translate_text
from contextual_understanding.context import apply_context
from speech_synthesis.synthesizer import synthesize_speech
from legal_ethical.compliance import ensure_compliance
from user_interface.interface import user_interface

def main():
    user_interface()
    recognized_text = recognize_speech(language='ta-IN')
    contextual_text = apply_context(recognized_text)
    translated_text = translate_text(contextual_text, src='ta', dest='en')
    compliant_text = ensure_compliance(translated_text)
    synthesize_speech(compliant_text, language='en')

if __name__ == "__main__":
    main()
