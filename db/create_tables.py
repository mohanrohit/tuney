import model

from song import Song
from playlist import PlayList
from song_playlist import SongPlayList

import logging
logging.basicConfig(format="[%(asctime)-15s] [%(name)s]: %(message)s", level=logging.DEBUG)

model.tuneydb.create_tables([
    Song,
    PlayList,
    SongPlayList
])
