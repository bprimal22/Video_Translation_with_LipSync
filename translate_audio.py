import whisper

model = whisper.load_model("large")
result = model.transcribe(audio="videos/Gosh_hindi_eng/Gosh-hindi.wav", language="Hindi", task="translate")
print(result["text"])

from TTS.api import TTS
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", gpu=True)
tts.tts_to_file(text=result['text'], language="en", speaker_wav="videos/Gosh_hindi_eng/ghosh_english.wav", file_path="videos/Gosh_hindi_eng/ghosh_eng_translation.wav")
