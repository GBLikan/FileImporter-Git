import unittest
from FileImporter.file.FileCompare import FileContext, compare_file_contexts, FileObject
from pathlib import Path
import os


class Test(unittest.TestCase):
    def test_compare_file_contexts(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        test_path = current_path + "/" + "test_files"
        ctx1 = FileContext()
        ctx1.populate(test_path + "/" + "rep1/")
        print("ORIG CTX ----------------------")
        ctx1.print_info()
        ctx2 = FileContext()
        ctx2.populate(test_path + "/" + "rep2/")
        print("DEST CTX ----------------------")
        ctx2.print_info()

        ctx3 = compare_file_contexts(ctx1, ctx2)

        print("ORIG NOT FOUND IN DEST------------------")
        ctx3.print_info()

        assert len(ctx3.files) == 2

        f1 = FileObject(test_path + "/" + "rep1/zorglub.csv", "zorglub.csv", 6)
        f1.print_info()
        f2 = FileObject(test_path + "/" + "rep1/subrep1/foobar.txt", "foobar.txt", 13)
        f2.print_info()
        assert ctx3.has_file(f1)
        assert ctx3.has_file(f2)


if __name__ == '__main__':
    unittest.main()