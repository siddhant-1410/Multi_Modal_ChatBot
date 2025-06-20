from pydub import AudioSegment
from gtts import gTTS
import os
import subprocess
import platform

def text_to_speech_with_gtts(input_text, mp3_path, wav_path):
    language = "en"

    # Save MP3
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(mp3_path)

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

    # Play WAV
    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'])
        elif os_name == "Darwin":
            subprocess.run(['afplay', wav_path])
        elif os_name == "Linux":
            subprocess.run(['aplay', wav_path])
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Call function
text_to_speech_with_gtts(
    input_text="Hi this is AI with Siddhant, converted to new version !",
    mp3_path="gtts_testing.mp3",
    wav_path="gtts_testing.wav"
)
