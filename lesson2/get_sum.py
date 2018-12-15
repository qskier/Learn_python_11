def get_summ(num_one, num_two):
	try:
		return int(num_one) + int(num_two)
	except ValueError:
		return 'Дайте целые значения для функции'
summa = get_summ(10.1111111,10)
print(summa)	