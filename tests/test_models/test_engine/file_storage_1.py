#!/usr/bin/python3
from models.engine.file_storage import FileStorage
storage = FileStorage()
assert hasattr(storage, "_FileStorage__objects")
assert isinstance(storage._FileStorage__objects, dict)
print("OK")
