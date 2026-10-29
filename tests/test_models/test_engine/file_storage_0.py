#!/usr/bin/python3
import sys
from models.engine.file_storage import FileStorage

try:
    storage = FileStorage()
    if hasattr(storage, "_FileStorage__file_path") and isinstance(storage._FileStorage__file_path, str):
        sys.stdout.write("OK\n")
        sys.stdout.flush()
    else:
        sys.stderr.write("Failed\n")
except Exception as e:
    sys.stderr.write(str(e))
