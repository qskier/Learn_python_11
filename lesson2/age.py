age = int(input('Сколько вам лет: '))

def main(age):
	if age <= 6:
		print ('Вам пора в детский сад')
	elif age <= 17:
		print ('Вам пора в школу')
	elif age <= 23:
		print ('Вам пора в университет')
	else: 
		print ('Вам пора на работу')

main(age)