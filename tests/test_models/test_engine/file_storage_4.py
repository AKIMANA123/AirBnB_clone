#!/usr/bin/python3
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

try:
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
        sys.stderr.write("Failed\n")
except Exception as e:
    sys.stderr.write(str(e))
