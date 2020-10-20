import os
from pydub import AudioSegment
AudioSegment.converter = "C:\\Users\\sopsla\\AppData\\Local\\ffmpeg\\bin\\ffmpeg.exe"

# exercise: store the three audio files in a new folder

# where are the sound files?
sound_folder = "C:\\Users\\sopsla\\Desktop\\session2b-sound\\raw"

# make a new folder
new_folder = "C:\\Users\\sopsla\\Desktop\\session2b-sound\\tmp"
if not os.path.isdir(new_folder):
    os.mkdir(new_folder)

# list all the files in the sound folder
sound_list = os.listdir(sound_folder)

# see what we've done
print(sound_list)

# save the sounds in the new folder
for sound_file in sound_list:
    sound_path = os.path.join(sound_folder, sound_file)
    sound = AudioSegment.from_wav(sound_path)
    sound.export(os.path.join(new_folder, sound_file))

# N.B. If you want to copy a file, you can consider using the package Shutil.
