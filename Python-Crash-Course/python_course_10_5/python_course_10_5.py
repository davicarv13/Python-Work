def record_response(response):
	with open('responses.txt', 'a') as file:
		file.write(response + '\n')

response = ''
print("Print 'q' to quit:")

while response != 'q':
	response = input('Enter your reason why you like programming:')
	if response != 'q':
		record_response(response)	
	else:
		print('Bye')
	
	