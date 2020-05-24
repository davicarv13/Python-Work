def make_album(artist_name, album_title, tracks_number = False):
	album = {"Artist's name": artist_name, "Album's title":album_title}
	if tracks_number:
		album["Track's Number"] = tracks_number
		return album
	else:
		return album

print(make_album("Taylor Swift", "Lover", 18))
print(make_album("Dua Lipa", "Future Nostalgia"))
print(make_album("Carly Rae Jepsen", "Dedicated"))


