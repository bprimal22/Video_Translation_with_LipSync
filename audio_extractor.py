# MP4 to Wav files

import subprocess

command = "ffmpeg -i videos/Gosh_hindi_eng/Gosh-Hindi.mp4 -ab 160k -ac 2 -ar 44100 -vn source/Gosh-hindi.wav"

subprocess.call(command, shell=True)
