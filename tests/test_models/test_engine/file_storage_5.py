#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
storage = FileStorage()
bm = BaseModel()
storage.new(bm)
storage.save()
storage._FileStorage__objects = {}
storage.reload()
key = "{}.{}".format(bm.__class__.__name__, bm.id)
assert key in storage.all()
print("OK")
