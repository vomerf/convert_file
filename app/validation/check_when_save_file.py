import os.path

from fastapi import HTTPException


def check_file(record):
    if not record.filename.split('.')[-1] == 'wav':
        raise HTTPException(status_code=404, detail='Формат входного файла должен быть .wav')
    file_location = f"files/{record.filename}"
    if os.path.isfile(file_location):
        raise HTTPException(status_code=404, detail='Такой файл уже существует')
