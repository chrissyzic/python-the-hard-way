i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num,

#Study Drill: Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
def count(max):
	start = 0
	numbers2 = []
	
	while start < max:
		print " The number started as: %d" % start
		numbers2.append(start)
		
		start = start + 1
		print "At the end of the loop the number is %d" % start
count(5)		
		
#Study Drill: Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.	
def count(max, add):
	start = 0
	numbers2 = []
	
	while start < max:
		print " The number started as: %d" % start
		numbers2.append(start)
		
		start = start + add
		print "At the end of the loop the number is %d" % start

count(8,2)

#Study Drill: Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?

def count(max):
	numbers3 = range(0, max+1)
	
	for i in numbers3:
		print "The current number is %d." % i
		
count(7)
		
