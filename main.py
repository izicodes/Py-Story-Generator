import time, os

# The menu
def menu():
	print("Welcome To Xia's Story Generator")
	time.sleep(0.75)
	print("\nHere is the list of the storylines available: ")
	print("""
[1] Humans and Aliens
[2] Your mother is a Goddess
[3] The Colour Killer
 """)
	time.sleep(0.75)
	answer = int(input("Select the number of the story you would like generated: "))
	
	if answer > 3 or answer < 0:
		print("\nThat number is not on the list. Please try again.")
		time.sleep(1.3)
		os.system("clear")
		menu()
	else:
		time.sleep(0.75)
		print("\nYour storyline game will load now . . .")
		time.sleep(1.3)
		return answer

# Section shown at the end of the story generated
def finishedStory(story):
	time.sleep(0.75)
	print("\nYour story will load now . . .")
	time.sleep(1.3)
	print(story)
	time.sleep(0.75)
	playAgain = input("Would you like to go to the main menu or end the game here? [continue/end]\n>> ")
	time.sleep(0.5)
	if playAgain == "continue":
		os.system("clear")
		menu()
	else:
		endPart()

# The Ending Screen
def endPart():
	os.system("clear")
	print("Welcome To Xia's Story Generator")
	print("\nThank you for playing! 💗")

# Displaying the title of the story
def displayTitle(title):
	print("Welcome To Xia's Story Generator")
	time.sleep(0.75)
	print(f"\n>> {title} \n")
	time.sleep(0.75)

# Storyline 1 
def humansAlienStory():
	displayTitle("Storyline 1: Humans and Aliens? 👨 👽")

	adjective = input("Give an adjective e.g. friendly, hostile, scared: ")
	alienName = input("Give a made-up alien race: ")
	language = input("Give a human language: ")
	randomNum = input("Give a random number: ")
	while True:
		spaceCraft = input("Select a number for a spacecarft name:\n[1] flying crafts\n[2] mother ships\n[3] starships\nEnter here: ")
		if spaceCraft == "1":
			spaceCraft = "flying crafts"
			break
		elif spaceCraft == "2":
			spaceCraft = "mother ships"
			break
		elif spaceCraft == "3":
			spaceCraft = "starships"
			break
		else:
			print("\n❌ That is not an option from the list. Please try again.\n")
			continue

	disease = input("Name a disease: ")
	majorEvent = input("Name a major event that allows all countries to compete in: ")		

	story1 = f"\n\nHumanity makes contact with an alien species - They are called {alienName}. They seem rather {adjective}, but also quite... baffled.\nAfter working out basic {language}, they ask us, 'We have not seen any {spaceCraft} leave this system for one of your many other colonies in {randomNum} local years. Why? Have you quarantined the system?'. We could only reply with, 'We had the {disease} spread across Earth, so you are correct, we were trying to keep you aliens safe!' The {alienName} saw through our lies. The truth was we put all our money into the {majorEvent}... we were too embarrassed to say it to the aliens..\n"

	finishedStory(story1)	

# Storyline 2
def motherGoddessStory():
	displayTitle("Storyline 2: Your mother is a Goddess ✨")

	# Variables for the story
	item = input("Name a random item: ")
	mythCreature = input("Name a myth creature but in the plural form: ").lower()
	motherName = input("Give a woman's name: ").capitalize()
	timeNum = input("Give a random number: ")
	while True:
		timeUnit = input("Select a time unit:\n[1] Weeks \n[2] Days \n[3] Hours \n[4] Minutes \n[5] Seconds \nEnter here: ")
		if timeUnit == "1":
			timeUnit = "weeks"
			break
		elif timeUnit == "2":
			timeUnit = "days"
			break
		elif timeUnit == "3":
			timeUnit = "hours"
			break
		elif timeUnit == "4":
			timeUnit = "minutes"
			break
		elif timeUnit == "5":
			timeUnit = "seconds"
			break
		else:
			print("\n❌ That is not an option from the list. Please try again.\n")
			continue
	powerName = input("Give a power ability name: ")						

	story2 = f"\n\nWhen you learned your mother was a goddess of {item}, things finally seemed to fall into place. The other demigods and {mythCreature} laughed at you, the only child born to the goddess of {item}, {motherName}. But your power was so much more than they could dream of. You had the power of {powerName}, which you kept secret for {timeNum} {timeUnit} from your mother and everyone. But how will you use your powers?\n"

	finishedStory(story2)

# Storyline 3
def colourKillerStory():
	displayTitle("Storyline 3: The Colour Killer 💛🔪")

	colour = input("Name a colour: ").capitalize()
	num = input("Give a number: ").lower()
	food = input("Give a singluar food item: ")
	userName = input("What is your name? ").capitalize()

	story3 = f"A serial killer known as “{colour}” always leaves behind exactly {num} clues per murder - {colour} paint left everywhere on the crime scene... as well as {food} left on a plate? Anyways, after months of being unable to catch her, the authorities turn to the only man smart enough to figure out {colour}’s Clues: the world-famous detective named {userName}. Only {userName} could bring justice to all the murders"

	finishedStory(story3)

# The Choices of storylines
answer = menu()
if answer == 1:
	os.system("clear")
	humansAlienStory()
elif answer == 2:
	os.system("clear")
	motherGoddessStory()
elif answer == 3:
	os.system("clear")
	colourKillerStory()
