#METHOD 1: Do this if your user knows the name of the file and how this function works
#Imports argv varaible from system that will hold the inputs the user types in the command line
from sys import argv

#Defines inputs
script, filename = argv

#Creates a variable containing the contents of the file 
txt = open(filename)

#Prints and intro so you know which file you're reading
print "Here's your file %r:" % filename
#Prints out the file with the contents of the file you want to open, by printing the variable created above
print txt.read()
txt.close()

#METHOD 2: Do this if your user doesn't know how this file/function works and will need to be prompted for the name of the file
#This is just to demonstrate another way to get 
print "Type the file name again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
