import random

cardlist = [
	'The Fool',
	'The Magician',
	'The High Priestess',
	'The Empress',
	'The Emperor',
	'The Hierophant',
	'The Lovers',
	'The Chariot',
	'Strength',
	'The Hermit',
	'Wheel of Fortune',
	'Justice',
	'The Hanged Man',
	'Death',
	'Temperance',
	'The Devil',
	'The Tower',
	'The Star',
	'The Moon',
	'The Sun',
	'Judgment',
	'The World'
]

cards = {
    'The Fool': 'New beginnings, optimism, trust in life',
    'The Magician': 'Action, the power to manifest',
    'The High Priestess': 'Inaction, going within, the subconscious',
    'The Empress': 'Abundance, nurturing, fertility, life in bloom!',
    'The Emperor': 'Structure, stability, rules and power',
    'The Hierophant': 'Institutions, tradition, society and its rules',
    'The Lovers': 'Sexuality, passion, choice, uniting',
    'The Chariot': 'Movement, progress, integration',
    'Strength': 'Courage, subtle power, integration of animal self',
    'The Hermit': 'Meditation, solitude, consciousness',
    'Wheel of Fortune': 'Cycles, change, ups and downs',
    'Justice': 'Fairness, equality, balance',
    'The Hanged Man': 'Surrender, new perspective, enlightenment',
    'Death': 'The end of something, change, the impermeability of all things',
    'Temperance': 'Balance, moderation, being sensible',
    'The Devil': 'Destructive patterns, addiction, giving away your power',
    'The Tower': 'Collapse of stable structures, release, sudden insight',
    'The Star': 'Hope, calm, a good omen!',
    'The Moon': 'Mystery, the subconscious, dreams',
    'The Sun': 'Success, happiness, all will be well',
    'Judgment': 'Rebirth, a new phase, inner calling',
    'The World': 'Completion, wholeness, attainment, celebration of life'
}

def printcard(cardname):

    sentence = cards[cardname]
    words = sentence.split(' ')
    wordcount = len(words)
    position = 0
    lines = 0

    print ' '
    print '-' * 40
    print '|'
    print '| %s' % cardname
    print '|'
    print '-' * 40
    print '|'

    while position < wordcount:

        if position % 3 == 0:
            
            lines += 1
            
            print "| %s" % words[position],

            if wordcount - 1 == position:

            	print ""

        elif position % 3 == 1:
            
            print words[position],

            if wordcount - 1 == position:

            	print ""        
        else:
        
        	print words[position]
        
        position += 1	

    filler = 10 - lines
    fillercount = 0
    while fillercount < filler:
        print '|'
        fillercount += 1

    print '-' * 40

def printallcards():

	for i in cards:

		printcard(i)

def printrandomcard():

	printcard(random.choice(cardlist))

def printmulticards():

	i = 0

	count = int(raw_input("How many cards would you like to see?\n> "))

	while i < count:

		printrandomcard()

		i += 1

def mainmenu():

	exit = False

	while exit == False:

		print "\nWould you like to:\n"
		print "1. See a card"
		print "2. See several cards"
		print "3. See all of the cards"
		print "4. Exit the program\n"

		selection = raw_input("> ")

		if selection == '1':
			printrandomcard()
		elif selection == '2':
			printmulticards()
		elif selection == '3':
			printallcards()
		elif selection == '4':
			quit(0)
		else:
			print "Please make a valid selection (1-4)!"

mainmenu()






