import bark
import soundfile


bark.preload_models()

text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs]
     But I also have other interests such as playing tic tac toe.
"""

audio_array = bark.generate_audio(text_prompt, history_prompt="en_speaker_1", text_temp=0.8, waveform_temp=0.7)

soundfile.write(file="mybarking-output-02.wav", data=audio_array, samplerate=bark.SAMPLE_RATE, format='WAV', subtype='PCM_16')