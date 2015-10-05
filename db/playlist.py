import peewee

import model

class PlayList(model.Model):
    title = peewee.CharField()

    class Meta:
        db_table = "playlists"
