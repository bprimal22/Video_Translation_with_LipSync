# MP4 to Wav files

import subprocess

command = "ffmpeg -i videos/Santacruz_spanish_eng/spanish.mp4 -ab 160k -ac 2 -ar 44100 -vn videos/Santacruz_spanish_eng/spanish.wav"

subprocess.call(command, shell=True)
