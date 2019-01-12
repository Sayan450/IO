"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
print(song_list)
assert len(song_list.songs) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs
song_list.sort_songs()
# test adding a new Song
song_list.add_song()
# test get_song()
song_list.get_song()
print(song_list)
# test getting the number of required and learned songs (separately)
# test saving songs (check CSV file manually to see results)
song_list.save_songs()