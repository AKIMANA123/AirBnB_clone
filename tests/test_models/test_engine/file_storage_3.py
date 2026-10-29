#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
storage = FileStorage()
bm = BaseModel()
storage.new(bm)
key = "{}.{}".format(bm.__class__.__name__, bm.id)
assert key in storage.all()
print("OK")
