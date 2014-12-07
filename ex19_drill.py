def inbox_count(incoming, answered):
	print "I received %d emails today and answered %d. That means I have %d waiting for me when I get in tomorrow." % (incoming, answered, incoming-answered)
	
inbox_count(100, 3)

received = 30
responded = 29

inbox_count (received, responded)
inbox_count(received, 10)
inbox_count(11+11, responded)
inbox_count(received+1, responded-2)

