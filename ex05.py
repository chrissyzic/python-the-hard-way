name = 'Zed A. Shaw'
age = 35 #not a lit
height = 74 #inches
height_cm = height * 2.54
weight = 180 #lbs
weight_kg = weight * 0.453
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He is %d inches (%d centimeters) tall." % (height, height_cm)
print "He's %d pounds heavy. That's %d kilograms" % (weight, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line might be tricking for some but I'm gonna kill it.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "Trying to figure out how %s works." % (name)
