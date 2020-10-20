import os
from pydub import AudioSegment, silence, effects
from pydub.playback import play

AudioSegment.converter = "C:\\Users\\sopsla\\AppData\\Local\\ffmpeg\\bin\\ffmpeg.exe"

# where are the sound files?
sound_folder = "C:\\Users\\sopsla\\Desktop\\session2b-sound\\raw"

# open a file
filename = "HF_recording.wav"
sound = AudioSegment.from_wav(os.path.join(sound_folder, filename))

# change the volume by a number of dBs
louder = sound[:2000] + 6
lower = sound[:2000] - 6

play(louder)
play(lower)

# in order to not confuse concatenation by volume change, you can also write:
louder = sound.apply_gain(6)
lower = sound.apply_gain(-6)

# maybe you want to change the volume in comparison to a given value.
# this is always relative to the maximum volume; maximum = 0.
print(louder.dBFS)

# say, we want the volume to be 6 dB lower than maximum; -6 dBFS
target_volume = -6
change = target_volume - louder.dBFS

# So this is how much we need to change the volume:
print(change)

# change it:
target_sound = sound.apply_gain(change)

# Extra: funny stuff
# reverse
backwards = sound.reverse()
play(backwards)

# Change the speed
hasty = effects.speedup(sound, playback_speed=1.5)
play(hasty)

# Fade-out
faded = backwards.fade_in(1000).fade_out(1000)
