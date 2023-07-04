from pathlib import Path
from time import ctime
import shutil

path = Path("testdir/testfile.py")

print(ctime(path.stat().st_ctime))
print(path.read_text())

source = Path("testdir/testfile.py")
target = Path() / "testfile.py"

shutil.copy(source, target)
