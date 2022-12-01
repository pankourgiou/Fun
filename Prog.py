from gtts import gTTS
import os
text = "To progress in a beautiful way"
tts = gTTS(text)
tts.save("hi.mp3")
os.system("hi.mp3")
