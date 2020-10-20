import os
from pydub import AudioSegment, silence
from pydub.playback import play
AudioSegment.converter = "C:\\Users\\sopsla\\AppData\\Local\\ffmpeg\\bin\\ffmpeg.exe"

# where are the sound files?
sound_folder = "C:\\Users\\sopsla\\Desktop\\session2b-sound\\raw"

# open a file
filename = "HF_recording.wav"
sound = AudioSegment.from_wav(os.path.join(sound_folder, filename))

# get duration
print(sound.duration_seconds)

# split it in two on the basis of duration
# PyDub works in milliseconds
halftime = (sound.duration_seconds / 2) * 1000
first_half = sound[:halftime]
second_half = sound[halftime:]

play(first_half)
play(second_half)

# concatenate them
wrong_order = second_half + first_half

# or add silence in between
silent_time = AudioSegment.silent(duration=2000)
wrong_order_silence = second_half + silent_time + first_half

# But we can't just ADD silence -- we can also split the sound file on the basis of silence!
# Minimum silence length = 2 seconds. How many pieces should that give us?
# What happens if we change the silence threshold?
words = silence.split_on_silence(wrong_order_silence, min_silence_len=2000, silence_thresh=-50)

# How to know which silence threshold to choose?
# Try it!
