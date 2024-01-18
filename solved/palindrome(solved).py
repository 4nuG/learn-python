''' Checks a 4-letter word for palindromicity '''
word = input('Enter a 4-letter word: ')
if ( word[0] == word[-1] and word [1] == word[-2]):
	print ('True')
else:
	print ('False')

