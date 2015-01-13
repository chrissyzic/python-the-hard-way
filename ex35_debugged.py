#This is Exercise 35, but reordered in a way that follows the flow of the game.
#I also updated some of the prompts to make it clearer what the player should enter.
#Oh and I fixed that weird way the original counted numbers in gold_room()

from sys import exit

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take (left or right)?"
	
	choice = raw_input()
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
	
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear (take honey, taunt the bear, or open the door)?"
	bear_moved = False
	
	while True:
		choice = raw_input()
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt the bear" and not bear_moved:
			print "The bear has moved from the door. What do you do (open the door or eat the honey?)"
			bear_moved = True
		elif choice == "taunt the bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "eat the honey" and bear_moved:
			dead("The bear gets angry you are eating his dinner and eats you instead.")
		elif choice == "open the door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
def gold_room():
	print "This room is full of gold. How many pieces do you take?"
	
	choice = raw_input("> ")
	if choice.isdigit() == True:
		how_much = int(choice)
	else:
		dead("Man, learn how to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
			
			

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stare at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input(">> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead ("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "Good job!"
	exit(0)

start()
