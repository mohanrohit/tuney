import db

db.model.tuneydb.create_tables([
    db.Song,
    db.PlayList,
    db.SongPlayList
])
