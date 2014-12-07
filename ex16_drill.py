from sys import argv

script, filename = argv

print "We're just going to read %r." % filename

target = open(filename)

print "OK, here's your file. I promise I didn't mess with it."
print target.read()

print "Now that you've read it, I'm going to close %r." % filename
target.close()
