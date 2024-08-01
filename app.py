from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/uploads/<path:path>')
def send_upload(path):
    return send_from_directory('uploads', path)

@app.route('/translate', methods=['POST'])
def translate():
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No audio file uploaded.'}), 400

    audio_file = request.files['audioFile']
    audio_path = os.path.join('uploads', audio_file.filename)
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return jsonify({'error': 'Google Speech Recognition could not understand audio.'}), 400
    except sr.RequestError as e:
        return jsonify({'error': f'Could not request results from Google Speech Recognition service; {e}'}), 400

    translated_text = GoogleTranslator(source='en', target='ta').translate(text)

    tts = gTTS(text=translated_text, lang='ta')
    translated_audio_path = os.path.join('uploads', 'translated_audio.mp3')
    tts.save(translated_audio_path)

    return jsonify({
        'transcribedText': text,
        'translatedText': translated_text,
        'translatedAudioUrl': f'/uploads/translated_audio.mp3'
    })

@app.route('/translate2', methods=['POST'])
def translate2():
    if 'audioFile2' not in request.files:
        return jsonify({'error': 'No audio file uploaded.'}), 400

    audio_file = request.files['audioFile2']
    audio_path = os.path.join('uploads', audio_file.filename)
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language='ta-IN')
    except sr.UnknownValueError:
        return jsonify({'error': 'Google Speech Recognition could not understand audio.'}), 400
    except sr.RequestError as e:
        return jsonify({'error': f'Could not request results from Google Speech Recognition service; {e}'}), 400

    translated_text = GoogleTranslator(source='ta', target='en').translate(text)

    tts = gTTS(text=translated_text, lang='en')
    translated_audio_path = os.path.join('uploads', 'translated_audio.mp3')
    tts.save(translated_audio_path)

    return jsonify({
        'transcribedText': text,
        'translatedText': translated_text,
        'translatedAudioUrl': f'/uploads/translated_audio.mp3'
    })


if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(port=5000)

