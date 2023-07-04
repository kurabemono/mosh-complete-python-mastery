from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")

# with ZipFile("files.zip", "w") as zip:
#     # get all files in "testdir" and its subdirectories and
#     # write them to "files.zip"
#     for path in Path("testdir").rglob("*.*"):
#         zip.write(path)

with ZipFile("files.zip", "r") as zip:
    info = zip.getinfo("testdir/testfile.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
