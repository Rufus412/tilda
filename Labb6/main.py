import pandas as pd
import numpy as np
import timeit
import re, mmap, time




columns = ["track_id", "song_id", "artist_name", "song_title"]


df = pd.read_csv(
    r"unique_tracks.txt",        # path to your file
    sep="<SEP>",        # use <SEP> as separator
    names=columns,      # assign column names
    engine="python",    # python engine handles multi-char separators
    encoding="utf-8"
)

all_songs = []
song_dict = {}


with open("unique_tracks.txt", "rb") as f:  # binary mode
    data = f.read()

with open("unique_tracks.txt", "rb") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)


matches = re.findall(rb"Silent\s+Night", data)
print(len(matches))

with open("unique_tracks.txt", "r", encoding='utf-8') as f:
    for line in f:
        all_songs.append(line.strip().split("<SEP>"))
        song_dict[line.split("<SEP>")[0]] = line.strip().split("<SEP>")[1:]

print(song_dict['TRMMMYQ128F932D901'])


#songs = df[df["artist_name"] == "Faster Pussy cat"]

def search_in_dict(track_id):
    return song_dict[track_id]


print(timeit.timeit(lambda: search_in_dict('TRVSGAU128F42749DA'), number=100))
print(timeit.timeit(lambda: df[df["artist_name"] == "F"], number=100))
print(timeit.timeit(lambda: [song for song in all_songs if song[2] == "F"], number=100))
print(timeit.timeit(lambda: re.findall(rb"Silent\s+Night", data), number=100))
print(timeit.timeit(lambda: re.findall(rb"Silent\s+Night", mm), number=100))




#print(songs)