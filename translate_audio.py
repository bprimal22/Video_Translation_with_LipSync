import whisper

model = whisper.load_model("small")
result = model.transcribe(audio="videos/Santacruz_spanish_eng/spanish.wav", language="Spanish", task="translate")
print(result["text"])

from TTS.api import TTS
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", gpu=True)
tts.tts_to_file(text=result['text'], language="en", speaker_wav="videos/Santacruz_spanish_eng/spanish.wav", file_path="videos/Santacruz_spanish_eng/eng_funny.wav")
