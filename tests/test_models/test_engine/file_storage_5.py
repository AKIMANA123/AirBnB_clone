#!/usr/bin/python3
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from models.engine.file_storage import FileStorage
    from models.base_model import BaseModel

    storage = FileStorage()
    bm = BaseModel()
    storage.new(bm)
    storage.save()
    storage._FileStorage__objects = {}
    storage.reload()
    key = "{}.{}".format(bm.__class__.__name__, bm.id)
    if key in storage.all():
        sys.stdout.write("OK\n")
        sys.stdout.flush()
    else:
        sys.stderr.write("Object not reloaded\n")
except Exception as e:
    sys.stderr.write(str(e) + "\n")
