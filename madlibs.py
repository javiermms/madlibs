from random import randint

nouns = ["cheese", "humans", "cow", "bear"]
verbs = ["waking", "running", "talking", "barking"]
adjectives = ["brave", "calm", "cool", "courageous"]
madlibs = ["Zoos are places where wild","N", "are kept in pens or cages so that","N", "can come and look at them.", "A", "Isnt it?"]

def create(word, item):
	if word == "Nouns":
		nouns.append(item)
		print(nouns)
	elif word == "Verbs":
		verbs.append(item)
		print(verbs)
	elif word == "Adjectives":
		adjectives.append(item)
		print(adjectives)
	else:
		print("List names are Case Sensitive make sure to type list names exactly as seen!")

def print_words():
	for i in madlibs:
		print(i + " ",  end = "")
		


def add_words():
	#num = shuffle(nouns)
	count = 1
	in_range = 0
	#delete outer for loop
	for num in range(len(madlibs)):
		
		print(in_range)
		print(str(count)+"!")

		for i in madlibs:
			if i == "N" and madlibs[count] == i:
				nums = len(nouns)
				madlibs[count] = nouns[in_range]
			elif i == "V" and i == madlibs[count]:
				nums = len(verbs)
				madlibs[count] = verbs[in_range]
			elif i == "A" and i == madlibs[count]:
				nums = len(adjectives)
				madlibs[count] = adjectives[in_range]
		#list range protections
		if in_range >= nums:
			in_range -= 1
		in_range += 1
		#change conditional statment for below
		if count < 6:
			count += 2
		
	return madlibs

#def shuffle(list):
	#return randint(0, len(list)-1)

def user_input(prompt):
	# the input function will display a message in the terminal
	# and wait for user input.
	user_input = input(prompt)
	return user_input


def select(function_code):
	# Choose MADLIB
	# #Choose List
	# elif function_code == "A":
	# 	item_index = user_input("Index Number?")
	# 	# Remember that item_index must actually exist or our program will crash.
	# 	read(item_index)


	if function_code == "C":

		input_one= user_input("Choose a list ---> Nouns, Verbs, Adjectives: ")

		if input_one == "Nouns" or  input_one == "Verbs" or  input_one == "Adjectives":
			input_two= user_input("Input word into list: ")
			create(input_one, input_two)
		else:
			print("Unknown Option")


	#Adds lists to madlib and then prints them
	if function_code == "I":
		#loop through every list and and add the words
		add_words()
		print_words()
		
	#Quit
	elif function_code == "Q" or function_code == "q":
		# This is where we want to stop our loop
		return False

	# Catch all
	#else:
		#print("Unknown Option")

	




	return True

running = True
while running:
	selection = user_input(
		"Press C to add to words, I to add words to Madlibs, Q to quit: ")
	running = select(selection)
