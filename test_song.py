"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.status == ""

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
print(song2)

print(song.status)
