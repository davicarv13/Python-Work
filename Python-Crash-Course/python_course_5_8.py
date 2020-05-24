usernames = ["admin", "davicarv13", "Achordetta", "drnim", "partager"]

if usernames:
	print("Ok")
	for username in usernames:
		if username.lower() == "admin":
			print("Hello " + username + ", would you like to see a status " +  
			"report?")
		else:
			print("Hello " + username + ", thank you for log-ging in again")
else:
	print("We need to find more users")