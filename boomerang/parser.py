#Text Command Parser for received commands

import re

def parseCommand(cmdStr):
	if re.match("(.+) every (\d+) dest (\d+)",cmdStr):
		print "true"
	else:
		print "oops"

parseCommand("testing every 12 dest 3035524795")