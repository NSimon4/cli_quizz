

questions = [
'What is the capital of Belgium ?',
'What is the capital of France ?'
]
answers = [
'Brussels',
'Paris'
]
i = 1
a = 0

def txt_display():
	global i
	global a
	if i == len(questions)+1:
		print 'End of lesson.'
		a = 1
	else:
		print questions[i-1]

def input_check():
	global i
	global a
	input = raw_input('Your response: ')
	if input == 'next': #skip / pass
		print 'Question skipped.'
		i = i + 1
		txt_display()
	elif input == 'exit':
		print 'Program terminated by user.'
		a = 1
	elif input == 'show answer':
		print answers[i-1]
		i = i + 1
		txt_display()
	elif input == answers[i-1]:
		print 'Correct!'
		i = i + 1
		txt_display()
	else:
		print 'Try again!'
		txt_display()


# MAIN

txt_display()
while a == 0:
	input_check()



