country = input('Your country: ')
age = input('Your age: ')
age = int(age)
if country == 'Taiwan' or 'taiwan' or 'TAIWAN' or 'Tai Wan' or 'tai wan' or 'TAI WAN':
	if age >= 18:
		print('allow to take drive test')
	else:
		print('not allow to take drive test')
