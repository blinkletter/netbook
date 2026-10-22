# fix_ids.py
import sys, uuid, nbformat

for path in sys.argv[1:]:
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        cell["id"] = uuid.uuid4().hex[:8]
    nbformat.write(nb, path)
    print("re-IDed", path)