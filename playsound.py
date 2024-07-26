from gtts import gTTS
import playsound

# Tamil text
tamil_text = "தமிழில் உரையாடல்"

# Convert text to speech
tts = gTTS(text=tamil_text, lang='ta')

# Save the audio file
tts.save("tamil_audio.mp3")

# Play the audio file
# playsound.playsound("tamil_audio.mp3")