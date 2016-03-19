'''
Игра виселица 

из списка компютер выбирает слово 
за 8 попыток нужно угадать слово
каждая неправильная попытка - к попыткам 
каждая буква записывается в словарь и выводится на екран
если правильная записываем в переменную


'''

import random


HANGMAN = (
				'''
			-------
			|     |
			|     
			|	  
			|   
			|     
			|	  
			|	 
			|	  
			|
			|
			------------
			''',
				'''
			-------
			|     |
			|     |
			|	  
			|   
			|     
			|	  
			|	 
			|	  
			|
			|
			------------
			''',
				'''
			-------
			|     |
			|     |
			|	  0
			|   
			|     
			|	  
			|	 
			|	  
			|
			|
			------------
			''',
				'''
			-------
			|     |
			|     |
			|	  0
			|   /-+-/
			|     
			|	  
			|	 
			|	  
			|
			|
			------------
			''',
				'''
			-------
			|     |
			|     |
			|	  0
			|   /-+-/
			|     |
			|	  
			|	 
			|	  
			|
			|
			------------
			''',
				'''
			-------
			|     |
			|     |
			|	  0
			|   /-+-/
			|     |
			|	  |
			|	 
			|	  
			|
			|
			------------
			''',
				'''
			-------
			|     |
			|     |
			|	  0
			|   /-+-/
			|     |
			|	  |
			|	 | 
			|	 | 
			|
			|
			------------
			''',

			'''
			-------
			|     |
			|     |
			|	  0
			|   /-+-/
			|     |
			|	  |
			|	 | |
			|	 | |
			|
			|
			------------
			''')

SLOVA = ('Киев','Одесса','Черкассы','Львов','Москва')
dek = []
MAX_LOS = len(HANGMAN)

los = 0

word = random.choice(SLOVA)
word = word.lower()

splin = '-' * len(word)
print("Дoбpo пожаловать в игру 'Виселица'. Удачи вам!")


while MAX_LOS > los and splin != word:
	print(HANGMAN[los])
	print("\nBы уже предлагали следующие буквы:\n",dek)
	print("\nОтгаданное вами в слове сейчас выглядит так:\n",splin)
	vopros = input('Введите букву ')
	vopros = vopros.lower()

	while vopros in dek:
		print("Bы уже предлагали букву",vopros)
		vopros = input('Введите букву ')
		vopros = vopros.lower()
	dek.append(vopros)

	if vopros in word:
		print("\nДa! Буква ",vopros," есть в слове!")
		new = ''
		for i in range(len(word)):
			if vopros == word[i]:
				new += vopros
			else:
				new += splin[i]
		splin = new
	else:
		print("\nK сожалению. буквы",vopros,"нет в слове.")
		los += 1
if MAX_LOS == los:
	print(HANGMAN[los])
	print("\nBac повесили!")
else:
	print("\nBы отгадали!")
	print("\nБылo загадано слово",word)