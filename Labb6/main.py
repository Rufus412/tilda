import pandas as pd
import numpy as np
import timeit
import re, mmap, time
import random

def binary_search(the_list, key):

    lower = 0
    upper = len(the_list) - 1

    index = int(upper/2)

    while( upper >= lower ):
        target = the_list[index][0]
        if target == key:
            return(key)
        elif (target > key):
            upper = index - 1
        elif ( target < key):
            lower = index + 1
        index = (lower + upper) // 2
    return ("None")


columns = ["track_id", "song_id", "artist_name", "song_title"]


df_og = pd.read_csv(
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

songs_sorted = all_songs.copy()
songs_sorted.sort(key = lambda x: x[0])

#songs = df[df["artist_name"] == "Faster Pussy cat"]

def search_in_dict(d, track_id):
    return d[track_id]


def test_functions(times, n):

    print("\ntestar för times =", times, ", n =", n)

    mindreLista = all_songs[0:n]
    mindreLista_sorted = songs_sorted[0:n]
    df = df_og[0:n]

    song_dict = {}

    for element in mindreLista:
        song_dict[element[0]] = element[1:]

    print("Hash i dict", timeit.timeit(lambda: search_in_dict(song_dict, mindreLista[0][0]), number=times), "s")

    print("Pandas linjär.", timeit.timeit(lambda: df[df["artist_name"] == "F"], number=times), "s")

    print("Vår binär:", timeit.timeit(
        lambda: binary_search(mindreLista_sorted, mindreLista[random.randint(0, len(mindreLista))][0]), number=times), "s")

    print("Python list compr:", timeit.timeit(lambda: [song for song in mindreLista if song[2] == "F"], number=times), "s")


test_functions(100, 250000)
test_functions(100, 500000)
test_functions(100, 1000000)


def bubble_sort(the_list, sort_index):

    return_list = the_list.copy()
    sorted = False

    while not sorted:
        sorted = True
        for j in range(len(the_list) - 1):
            if (return_list[j][sort_index] > return_list[j+1][sort_index]):
                temp = return_list[j][sort_index]
                return_list[j][sort_index] = return_list[j+1][sort_index]
                return_list[j+1][sort_index] = temp
                sorted = False

    return return_list

def quick_sort(the_list, sort_index):
    if len(the_list) <= 1:
        return the_list

    stack = [(0, len(the_list) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = the_list[start][sort_index]
        low = start + 1
        high = end

        while True:
            while low <= high and the_list[high][sort_index] >= pivot:
                high -= 1
            while low <= high and the_list[low][sort_index] <= pivot:
                low += 1
            if low > high:
                break
            the_list[low], the_list[high] = the_list[high], the_list[low]

        the_list[start], the_list[high] = the_list[high], the_list[start]

        # Push the indices of the sub-arrays onto the stack
        stack.append((start, high - 1))
        stack.append((high + 1, end))

    return the_list

def is_sorted(the_list, sort_index):
    sorted = True
    for i in range(len(the_list) - 1):
        if the_list[i][sort_index] > the_list[i+1][sort_index]:
            sorted = False

    return sorted


songs2 = all_songs[0:1000]

def testa_sorteringar(song_list):

    songs2_1 = song_list.copy()
    songs2_2 = song_list.copy()

    print("\nBubble sort.", timeit.timeit(lambda: bubble_sort(songs2_1, 2), number=1), "s")
    print("Quicksort.", timeit.timeit(lambda: quick_sort(songs2_2, 2), number=1), "s")


testa_sorteringar(all_songs[0:1000])
testa_sorteringar(all_songs[0:10000])
testa_sorteringar(all_songs[0:100000])
testa_sorteringar(all_songs[0:1000000])

