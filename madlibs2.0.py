from random import randint

nouns = list()
verbs = list()
adjectives = list()
madlibs = ["Dear", "N", "You are extremly","A", "and I", "V", "you! I want to kiss your", "N", "6011 1234 5678 9012 times. You make my", "N", "burn with desire. When I first saw you, I", "A", "stared at you and fell in love. Will you", "V", "out with me? Don`t let your parents discourage you,", "N", "are just jealous.", "Your's forever,", "N"]
output = ["Dear", "N", "You are extremly","A", "and I", "V", "you! I want to kiss your", "N", "6011 1234 5678 9012 times. You make my", "N", "burn with desire. When I first saw you, I", "A", "stared at you and fell in love. Will you", "V", "out with me? Don`t let your parents discourage you,", "N", "are just jealous.", "Your's forever,", "N"]


def create(word):
	count = 0
	while count <= len(madlibs) - 1:
		if madlibs[count] == "N":
			nouns.append(word)
		elif madlibs[count] == "V":
			verbs.append(word)
		elif madlibs[count] == "A":
			adjectives.append(word)
		count += 1


def print_words():
	for i in output:
		print(i + " ",  end = "")

def add_words():
	count = 0
	
	while count <= len(madlibs) - 1:
		if madlibs[count] == "N":
			output[count] = nouns[count]
		elif madlibs[count] == "V":
			output[count] = verbs[count] 
		elif madlibs[count] == "A":
			output[count] = adjectives[count]
		count += 1
	return output

# def check_madlibs():
# 	for words in madlibs:
# 		for word in madlibs:
# 			if words == word:
# 				madlibs[word] = nouns[randint(0, len(nouns) - 1)]

		

def user_input(prompt):
	# the input function will display a message in the terminal
	# and wait for user input.
	user_input = input(prompt)
	return user_input

def select(function_code):
	
	if function_code == "P":
		create(user_input("Enter a person's name: "))
		create(user_input("Enter an adjective: "))
		create(user_input("Enter a verb: "))
		create(user_input("Enter a body part: "))
		create(user_input("Enter a noun: "))
		create(user_input("Enter a adverb: "))
		create(user_input("Enter a verb: "))
		create(user_input("Enter a plural pronoun: "))
		create(user_input("Enter a person's name: "))
		add_words()
		print_words()		
	#Quit
	elif function_code == "Q" or function_code == "q":
		# This is where we want to stop our loop
		return False
	else:
			print("Unknown Option")
	return True

running = True
while running:
	selection = user_input(
		"Press P play or Q to quit: ")
	running = select(selection)