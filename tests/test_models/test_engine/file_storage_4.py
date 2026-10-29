#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
if os.path.exists("file.json"):
    os.remove("file.json")
storage = FileStorage()
bm = BaseModel()
storage.new(bm)
storage.save()
assert os.path.exists("file.json")
print("OK")
