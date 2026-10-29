#!/usr/bin/python3
import sys
from models.base_model import BaseModel

try:
    bm = BaseModel()
    if bm.id and bm.created_at and bm.updated_at:
        sys.stdout.write("OK\n")
        sys.stdout.flush()
    else:
        sys.stderr.write("Failed\n")
except Exception as e:
    sys.stderr.write(str(e))
