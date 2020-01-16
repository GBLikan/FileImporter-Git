from FileImporter.file.FileCompare import FileObject, FileContext, compare_file_contexts, compare_file_objects


def run():
    ctx1 = FileContext()
    ctx1.populate("/home/likan/test/rep1/")
    ctx2 = FileContext()
    ctx2.populate("/home/likan/test/rep2/")

    compare_file_contexts(ctx1, ctx2)