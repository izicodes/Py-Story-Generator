import time, os

points = 0

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

# The Ending Screen
def endPart():
	os.system("clear")
	print("Welcome To Xia's Story Generator")
	print("\nThank you for playing! 💗")

# Storyline 1 
def humansAlienStory():
	print("Welcome To Xia's Story Generator")
	time.sleep(0.75)
	print("\n>> Storyline 1: Humans and Aliens? 👨 👽 \n")
	time.sleep(0.75)

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

	time.sleep(0.75)
	print("\nYour story will load now . . .")
	time.sleep(1.3)
	print(story1)
	time.sleep(0.75)
	playAgain = input("Would you like to go to the main menu or end the game here? [continue/end]\n>> ")
	if playAgain == "continue":
		os.system("clear")
		menu()
	else:
		endPart()	




answer = menu()
if answer == 1:
	os.system("clear")
	humansAlienStory()


story1 = "Humanity makes contact with an alien species. They seem rather friendly, but also quite... baffled. After working out basic English, they ask us, 'We have not seen any starship leave this system for one of your many other colonies in 297,591 local years. Why? Have you quarantined the system?'"

story2 = "When you learned your mother was a goddess, things finally seemed to fall into place. The other demigods laughed at you, the only child born to the goddess of the hearth, Hestia. But your power was so much more than they could dream of."

story3 = "A serial killer known as “Blue” always leaves behind exactly three clues per murder. After months of being unable to catch her, the authorities turn to the only man smart enough to figure out Blue’s Clues: the world-famous detective named Steve."