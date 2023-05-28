def save_in_local_storage(record, file_location):
    with open(file_location, "wb") as file_object:
        file_object.write(record.file.read())
