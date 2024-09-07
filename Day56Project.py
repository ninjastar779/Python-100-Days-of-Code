import csv
import os

with open('MostStreamedSongs.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the first line
    artists = {}
    for row in reader:
        artist = row[3]
        song = row[1]
        if artist not in artists:
            artists[artist] = []
        artists[artist].append(song)

for artist, songs in artists.items():
    folder = os.path.join(os.getcwd(), artist)
    if not os.path.exists(folder):
        os.makedirs(folder)
    for song in songs:
        with open(os.path.join(folder, song + '.txt'), 'w') as f:
            pass

