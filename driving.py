country = input('Your country: ')
age = input('Your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('allow to take drive test')
	else:
		print('not allow to take drive test')
elif country == 'US':
	if age >= 16:
		print('allow to take driver test')
	else:
		print('not allow to take drive test')
else:
	print('please only enter "Taiwan" or "US"')