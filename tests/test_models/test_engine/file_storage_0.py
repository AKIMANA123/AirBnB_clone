#!/usr/bin/python3
from models.engine.file_storage import FileStorage
storage = FileStorage()
assert hasattr(storage, "_FileStorage__file_path")
assert isinstance(storage._FileStorage__file_path, str)
print("OK")
