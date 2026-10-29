#!/usr/bin/python3
from models.base_model import BaseModel
bm = BaseModel()
old_updated = bm.updated_at
bm.save()
assert old_updated != bm.updated_at
print("OK")
