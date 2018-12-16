import csv

users = [
	{'name': 'Маша', 'age': 25, 'job': 'Scientist'},
	{'name': 'Вася', 'age': 22, 'job': 'Programmer'},
	{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
]

with open('users.csv', 'w', encoding='windows-1251', newline='') as csvfile:
	fieldsnames = ['name', 'age', 'job']
	writer = csv.DictWriter(csvfile, fieldsnames, delimiter=',')

	writer.writeheader()
	for user in users:
		writer.writerow(user)
