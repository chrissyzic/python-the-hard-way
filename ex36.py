from sys import exit

def alarm():
#I want to loop this, so if you hit snooze too many times it triggers late()
    print "Your alarm goes off. Do you get up or hit snooze?"
	
    choice = raw_input()
    snooze count = 

    if snooze_count == 4:
        late("You overslept.")
    elif choice == 'get up':
        awake()
    elif choice == 'snooze':
        print "It's ten minutes later."
        snooze_count = snooze_count + 1
        alarm()
    else:
        print "I don't understand."
        print "Tell me more"

def awake():
    
    print "Are you going to shower or just get dressed?"
	
    choice = raw_input()
	
    if choice == 'shower':
        print "OK time to walk to the bathroom."
        bathroom()
    elif choice == 'get dressed':
        closet()
    else:
        print "Nope, not an option."

def bathroom():

    print "What are you gonna do: wash your hair, shave, or just rinse?"

    choice = raw_input()

    if choice == 'wash hair':
        print "washing hair lala"
    elif choice == 'shave':
        late("Shaving takes too long.")
    else:
        print "say wha"
    

def closet():
    
    print "Oh shit, you have no underwear. Are you going to do laundry, go commando, or flip it inside out?"

    choice = raw_input()

    if choice == 'do laundry':
        late("Laundry takes forever.")
    elif choice == 'go commando':
        print "ew"
    elif choice == "inside out":
        print "extra ew"
    else:
        print "ewewew"
        
def outfit():
    
    print "Are you going to wear a dress or a whole outfit?"

    choice = raw_input()

    if choice =='dress':
        on_time()
    elif choice == "whole outfit":
        late("You took to long to pick out your clothes.")
    else:
        print "yike"
            
def late(reason):
    
    print "{0} Now you're late.".format(reason)  
    exit()

def on_time():

    print "It's 8:59 and you're in the office. Good job!"
    exit()

alarm()
		
