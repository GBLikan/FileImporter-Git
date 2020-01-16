from typing import List
from glob import iglob
import os
import ntpath


class FileObject(object):

    def __init__(self, filepath, filename, size):
        self.filepath = filepath
        self.filename = filename
        self.size = size

    def print_info(self):
        print(self.filepath + " | " + self.filename + " | " + str(self.size))


class FileContext:
    files: List[FileObject] = []

    def __init__(self) -> None:
        super().__init__()

    def populate(self, path: str):
        for filepath in iglob(path + '**/*', recursive=True):
            if not ntpath.isdir(filepath) :
                filestat = os.stat(filepath)
                f = FileObject(filepath, ntpath.basename(filepath), filestat.st_size)
                f.print_info()
                self.files.append(f)


def compare_file_objects(f1: FileObject, f2: FileObject):
    return f1.filename == f2.filename and f1.size == f2.size


def compare_file_contexts(fctx1: FileContext, fctx2: FileContext):
    files_not_found: List[FileObject] = []

    for fOrigin in fctx1.files:
        found: bool = False
        for fDest in fctx2.files:
            found = compare_file_objects(fOrigin, fDest)
        if not found:
            files_not_found.append(fOrigin)
            print("NOT FOUND :")
            fOrigin.print_info()

    return files_not_found


