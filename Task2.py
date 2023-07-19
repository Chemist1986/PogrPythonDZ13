import os

class FilePathError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def extract_file_info(file_path):
    try:
        if not os.path.isabs(file_path):
            raise FilePathError("Путь должен быть абсолютным.")
        
        path, filename = os.path.split(file_path)
        filename, extension = os.path.splitext(filename)
        
        return path, filename, extension
    except FilePathError as e:
        raise e
    except Exception as e:
        raise FilePathError("Ошибка при извлечении информации о файле.")


try:
    file_path = "/path/to/file.txt"
    path, filename, extension = extract_file_info(file_path)
    
    print("Путь:", path)
    print("Имя файла:", filename)
    print("Расширение файла:", extension)
except FilePathError as e:
    print("Ошибка при извлечении информации о файле:", e.message)