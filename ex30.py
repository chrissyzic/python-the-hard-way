#The next three lines define the variables people, cars, and trucks.
people = 3
cars = 40
trucks = 15

#This evaluates if the value of cars is larger than the value of people
if cars > people:
#If cars > people, this line prints the "We should take the cars" statement.
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
	
if cars > people and trucks > people:
	print "We can take whatever vehicle we want."
else:
	print "Do whatever makes the most sense."

#We should take the cars.
#Maybe we could take the trucks.
#Alright, let's take the trucks.
