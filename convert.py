from pydub import AudioSegment
sound = AudioSegment.from_mp3("/root/Documents/dev/hi_cathleen/hp.mp3")
sound.export("/root/Documents/dev/hi_cathleen/hp.wav", format="wav")