from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

#We could do these two commands on one line like indata = open(from_file).read() - but it's not necessarily recommended. You could ALSO do it by adding a semicolon between them and removing the line break
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bites long." % len(indata)

print "Does the output file exist? %r." % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close() #This isn't necessary if you use the (not recommended) shortcut of indata = open(filename).read()
