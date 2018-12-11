ph = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую', 'Сколько тебе лет?':'Сложный вопрос' }

def ask_user():
	while True:
		string_1 = input('Задай мне какой-нибудь вопрос ')
		if string_1 == ph[0]:
			print ('Бомба')
			break
		else:
			print('Пиши еще')
ask_user()
