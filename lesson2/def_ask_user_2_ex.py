phrases = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую', 'Сколько тебе лет?':'Сложный вопрос' }

def ask_user():
	try:
		while True:
		
			string_1 = input('Задай мне какой-нибудь вопрос ')
			if string_1 in phrases.keys():
				print (phrases[string_1])
				break
			else:
				print('Пиши еще') 
	except KeyboardInterrupt:
		print('зря так рано уходишь')	
			
ask_user()
