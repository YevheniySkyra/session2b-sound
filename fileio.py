import os
from pydub import AudioSegment
from pydub.playback import play
from matplotlib.pyplot import plot, show

# Use this line of code if you can't add ffmpeg to your PATH (as per instructions)
# doesn't hurt to add it ...
AudioSegment.converter = "C:\\Users\\sopsla\\AppData\\Local\\ffmpeg\\bin\\ffmpeg.exe"

# Use the os module. Works for UNIX, Windows, MacOS...
# e.g., to get working directory
os.getcwd()

# or change working directory
# os.chdir("path")

# where are the sound files?
sound_folder = "C:\\Users\\sopsla\\Desktop\\session2b-sound\\raw"

# load a sound file
sound_path = os.path.join(sound_folder, "HF_recording.wav")
sound = AudioSegment.from_wav(sound_path)

# Because of using AudioSegment, the variable "sound" is now of class "AudioSegment.
# What a class is, we will discuss later. For now, it is only necessary to know
# that a class has ATTRIBUTES. 'AudioSegment' has attributes like 'channels', 'dBFS', 'duration_seconds'.
# Let's see what that means.
print(sound.duration_seconds)

# Or access several of them in one line
# dBFS: decibels relative to full scale
# full scale; maximum possible digital level
print(sound.channels, sound.dBFS, sound.duration_seconds)

# Play a sound
play(sound)

# Visualize a sound
# A sound is a time-series, like EEG or MEG data.
# It is an array of samples with a specific value. PyDub can give us this so we can plot it:
array = sound.get_array_of_samples()

# Take a look at the array
print(array)

# Now we plot it. If you don't run in console, you have to type show() to actually open a window with the plot.
plot(array)
show()

# Change the extension: wav to mp3
# first: split the extension and the name using os.path.splitext
# N.B.: the function os.path.split() splits the path to the folder from the filename.
filename, extension = os.path.splitext(sound_path)

# Export the sound to change the extension
new_filename = os.path.join(sound_folder, filename) + ".mp3"
sound.export(new_filename, format="mp3")

# we can also remove it again. (Make sure to close any open console windows.)
os.remove(new_filename)

# How can we make a new folder to save our sound files?
new_folder = "C:\\Users\\sopsla\\Desktop\\session2b-sound\\tmp"
if not os.path.isdir(new_folder):
    os.mkdir(new_folder)

# How can we list all files in one folder?
print(os.listdir(sound_folder))

# exercise: store the three audio files in a new folder.
