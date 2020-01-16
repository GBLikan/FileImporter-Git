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

    def __init__(self) -> None:
        self.files: List[FileObject] = []
        super().__init__()

    def populate(self, path: str):
        for filepath in iglob(path + '**/*', recursive=True):
            if not ntpath.isdir(filepath):
                filestat = os.stat(filepath)
                f = FileObject(filepath, ntpath.basename(filepath), filestat.st_size)
                self.files.append(f)

    def print_info(self):
        for f in self.files:
            f.print_info()

    def add_file(self, f: FileObject):
        self.files.append(f)

    def has_file(self, f: FileObject):
        for f_dest in self.files:
            found = compare_file_objects(f, f_dest)
            if found:
                return found
        return found


def compare_file_objects(f1: FileObject, f2: FileObject):
    return f1.filename == f2.filename and f1.size == f2.size


def compare_file_objects_strict(f1: FileObject, f2: FileObject):
    return f1.filename == f2.filename and f1.size == f2.size and f1.filepath == f2.filepath


def compare_file_contexts(fctx1: FileContext, fctx2: FileContext):
    files_not_found_context = FileContext()

    for fOrigin in fctx1.files:
        found: bool = fctx2.has_file(fOrigin)
        if not found:
            files_not_found_context.add_file(fOrigin)

    return files_not_found_context
