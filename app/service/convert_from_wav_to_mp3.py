from pydub import AudioSegment


def convert(record):
    src = f"files/{record.filename}"
    dst = f"files/{record.filename.split('.')[0]}.mp3"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    return dst
