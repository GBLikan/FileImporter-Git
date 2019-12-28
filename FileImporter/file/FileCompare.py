from typing import List
from glob import iglob


class FileCompareObject:

    def __init__(self, filename):
        self.filename = filename


class FileCompareContext:
    files: List[FileCompareObject] = []

    def __init__(self) -> None:
        super().__init__()

    def populate(self, path: str):
        for filename in iglob(path + '**/*', recursive=True):
            print(filename)
            self.files.append(FileCompareObject(filename))
