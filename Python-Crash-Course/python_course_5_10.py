current_users = ["admin", "davicarv13", "Achordetta", "drnim", "partager"]

new_users = ["drnim", "Partager", "tiozao", "lyn"]

for user in new_users:
	if user.lower() in current_users:
		print("Sorry, " + user + ", this username is not available")
	else:
		print("This username is available")

