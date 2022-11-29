import time



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
		print("That number is not on the list. Please try again.")
	
	time.sleep(0.75)
	print("\Your storyline game will load now . . .")
	return answer


answer = menu()

if answer == 1:

def humansAlienStory():
	print("Hello")
	

story1 = "Humanity makes contact with an alien species. They seem rather friendly, but also quite... baffled. After working out basic English, they ask us, 'We have not seen any starship leave this system for one of your many other colonies in 297,591 local years. Why? Have you quarantined the system?'"

story2 = "When you learned your mother was a goddess, things finally seemed to fall into place. The other demigods laughed at you, the only child born to the goddess of the hearth, Hestia. But your power was so much more than they could dream of."

story3 = "A serial killer known as “Blue” always leaves behind exactly three clues per murder. After months of being unable to catch her, the authorities turn to the only man smart enough to figure out Blue’s Clues: the world-famous detective named Steve."