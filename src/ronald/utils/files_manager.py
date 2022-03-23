from ronald.utils.common_include import *

from pathlib import Path
import shutil


class FileInfo():
    def __init__(self, file_path, file_mode='w'):
        self.file_path = file_path
        self.file_mode = file_mode
        self.file = open(file_path, file_mode)

    def close(self):
        self.file.close()


class FilesManager():
    def __init__(self, folder):
        self.folder = folder
        self.files: Dict[str, FileInfo] = {}

    def CreatFile(self, file_name, mode='w'):
        file_path = Path(self.folder) / file_name
        new_file = FileInfo(str(file_path), mode)
        self.files[file_name] = new_file
        return new_file.file

    def GetFile(self, file_name):
        return self.files[file_name].file

    def ReadFile(self, file_name):
        with open(self.files[file_name].file_path, 'r') as f:
            return f.read()

    def Close(self, file_name):
        if file_name in self.files:
            self.files[file_name].close()

    def CloseAll(self):
        for file in self.files.values():
            file.file.flush()
            file.close()

    @staticmethod
    def CreateFolder(folder, remove_old=True):
        folder_path = Path(folder)
        if folder_path.exists() and remove_old:
            shutil.rmtree(str(folder_path))
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
