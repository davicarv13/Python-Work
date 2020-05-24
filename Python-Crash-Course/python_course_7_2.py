people_number = input("How many people are in their dinner group?")

people_number = int(people_number)

if people_number >= 1 and people_number <= 8:
	print("Table is available")
elif people_number > 8:
	print("Wait for table")