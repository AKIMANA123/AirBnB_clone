#!/usr/bin/python3
import sys
import os

# Ensure project root is in sys.path so 'models' can always be imported
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from models.engine.file_storage import FileStorage
    from models.base_model import BaseModel

    if os.path.exists("file.json"):
        os.remove("file.json")
    storage = FileStorage()
    bm = BaseModel()
    storage.new(bm)
    storage.save()
    if os.path.exists("file.json"):
        sys.stdout.write("OK\n")
        sys.stdout.flush()
    else:
        sys.stderr.write("file.json was not created\n")
except Exception as e:
    sys.stderr.write(str(e) + "\n")
