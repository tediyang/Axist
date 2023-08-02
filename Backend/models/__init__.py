#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv

# DBSTORAGE
if getenv('AXIST_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    pass
storage.reload()
