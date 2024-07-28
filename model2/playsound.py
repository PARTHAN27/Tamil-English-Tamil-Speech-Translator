from gtts import gTTS
import playsound

# Tamil text
langtext = "என் பெயர் பார்த்தன்"

# Convert text to speech
tts = gTTS(text=langtext, lang='ta')

# Save the audio file
tts.save("audio.mp3")

# Play the audio file
# playsound.playsound("audio.mp3")
