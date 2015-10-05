import peewee

import song
import playlist

import model

class SongPlayList(model.Model):
    song = peewee.ForeignKeyField(song.Song)
    playlist = peewee.ForeignKeyField(playlist.PlayList)

    class Meta:
        db_table = "songs_playlists"
        primary_key = False
