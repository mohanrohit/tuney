import peewee

import model

class Song(model.Model):
    title = peewee.CharField()
    length = peewee.IntegerField()
    url = peewee.TextField()

    class Meta:
        db_table = "songs"
