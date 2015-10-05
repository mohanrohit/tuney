import os
import peewee

tuneydb = peewee.SqliteDatabase(os.path.dirname(__file__) + "/tuney.db")

class Model(peewee.Model):
    class Meta:
        database = tuneydb
