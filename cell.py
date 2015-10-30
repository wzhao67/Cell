import sys

inventory=[]
#to add to it
#inventory.append("something")
#inventory.remove()
#determine if player has an item
#try:
#inventory.index("item")
#except:
#print "Player doesn't have item"

def start():
    print "\nThe journey begins."
    print  
    counter = 0;
    while(1):
        prompt = raw_input('''Type "start":\n''')
        prompt = prompt.lower()   
        if prompt == 'start':
            wake_up()
        elif counter > 0:
            print '''Type 'start'. Not the brightest, are you?'''
        else:
            print '''That's not an option. Trust me. Type "start." '''
            counter = counter + 1

    
def wake_up():
    print '''
    You wake up feeling dizzy. What happened? You think to yourself. The past few days are a blur. 
    \n  Playing ping pong with alcohol...
    \n  Naming plastic cups after royalty...
    \n  Watching too much Netflix...'''
    print

    while(1):
        prompt = raw_input('''Will you "sit up" or just "lay there"?\n''')
        prompt = prompt.lower()
        if prompt == "sit up":
            sit_up()
        elif prompt == 'lay there':
            print '''
        You lie in your pool of metaphorical filth and contemplate your broken dreams.\n
        Eventually you sit up.'''
            sit_up()
        else:
            print ("Unfortunately there are only two things that you can/will do...")
    
def sit_up():
    print '''
    "Where am I?" you talk out loud, because that's the normal thing to do.\n
    "You will find out in due time," says a cool, female voice.\n
    You start and jump to your feet. '''
    counter = 0
    
    while(1):
        if counter<=1:
            prompt = raw_input('''What do you ask the voice? "Who are you?", "Where am I?" or "I'm scared. I want my mommy!"\n ''')
        else:
            prompt = raw_input('''What do you ask the voice? "Who are you?" or "Where am I?"\n ''')
        prompt = prompt.lower()
        
        if "who" in prompt:
            print '''
        "My name is Em. I am the computer control unit of Biotom, a highly advanced transportation device
        designed to enter biological systems. Biotom was designed to perform medical operations at the cellular
        level. I am its companion, and you are mine." '''
            look_around()
        elif "where" in prompt:
            print '''
        "We are inside the Biotom, a highly advanced transportation device
        designed to enter biological systems. Biotom was designed to perform 
        medical operations at the cellular level. 
        My name is Em. I am Biotom's computer control unit." 
            '''
            look_around()
        elif ("mommy" in prompt) or ("scared" in prompt):
            if counter==0:
                print '''
            "Please calm down. Your survival is crucial to our operations." '''
                counter = counter + 1
            elif counter==1:
                print ''' 
            "Let me just wait for you to stop freaking out. Then we can talk." '''
                counter = counter + 1
            else:
                print '''
            "My goodness. You're a university student. Calm down!" '''
                
        else:
            print ('''
            "I don't want to answer to that right now," she says stoicly.''')

def look_around():
    print '''
    You try to absorb the information. \n
    You try to bend your head around it. \n
    So...\n     You're in some sort of spaceship...but not in space...and it's really tiny?\n
    Just then the lights come on and the ship roars to life. 
    You see a series of controls and blinking lights around you.
    Before you lies a large window, looking towards the outside of the ship.     
    '''
    while(1):
        prompt = raw_input('''Will you "look outside" or just "go back to sleep"?\n''')
        prompt = prompt.lower()
        if "look" in prompt:
            mission()
        elif "sleep" in prompt:
            print '''
        You decide to go to bed like a good college student.\n
        But you eventually wake up. \n
        Everybody does. \n
        You look outside...\n'''
            mission()
        else:
            print ("Unfortunately there are only two things that you can/will do...")

def mission():
    print '''
    Outside the Biotom's front window, \
    you see a large, gelatinous surface embedded with globulous objects. \
    A flurry of activiy is going on on the surface. \
    Things were flying across it to the other side. \
    Other objects are coming out of it. 
    
    '''
    while(1):
        prompt = raw_input('''Will you "rub your eyes" or "ask Em what it is"?\
        If you know what this gooey surface is, let Em know. \n''')
        prompt = prompt.lower()
        if "rub" in prompt or "eye" in prompt:
            print '''
            "You are not dreaming," says Em. "Do you know what this is?"
            '''
        elif "ask" in prompt or "what" in prompt:
            print '''
        "This is the cell membrane," Em says matter-of-factly. 
        "You must be wondering why we are here. We are to infiltrate this cell and \
        replace a faulty gene in the nucleus. It goes without saying that you must \
        complete this mission without dying."
        '''
            get_ions()
        elif "membrane" in prompt:
            print '''
            "Correct," says Em. "I am glad you are so smart. \
            It reduces the probability of you dying. \
            You must be wondering why we are here. We are to infiltrate this cell and \
            replace a faulty gene in the nucleus.
            '''
            get_ions()
        else:
            print ("You don't feel like doing that...")

def startstartget_ions():
    sys.exit()

start()
exit()
