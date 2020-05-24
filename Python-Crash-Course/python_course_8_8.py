def make_album(artist_name, album_title, tracks_number = False):
	album = {"Artist's name": artist_name, "Album's title":album_title}
	if tracks_number:
		album["Track's Number"] = tracks_number
		return album
	else:
		return album

artist_name = ''
album_title = ''
albums = []

print("Enter 'q' to leave");
while artist_name != 'q' or album_title != 'q':
	artist_name = input("Enter artist's name:")

	if artist_name == 'q':
		break

	album_title = input("Enter album title's:")

	if album_title == 'q':
		break

	albums.append(make_album(artist_name, album_title))

for album in albums:
	print(album)


