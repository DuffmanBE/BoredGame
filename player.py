#!/usr/bin/env python

CHARACTERS = ["char1", "char2", "char3", "char3", "char5"]
AVAILABLE_CHARACTERS = CHARACTERS[:]

def makePlayer(character):
	global AVAILABLE_CHARACTERS
	if character in AVAILABLE_CHARACTERS:
		AVAILABLE_CHARACTERS.remove(character)
		return {'player' : True , 'character' : character , 'points' : 0 , 'items' : list() }
	else:
		return False

def getAvailableCharactgers():
	global AVAILABLE_CHARACTERS
	return AVAILABLE_CHARACTERS

def playerDecrPoints(player):
	player['points'] = player['points']-1

def playerIncrPoints(player):
	player['points'] = player['points']+1

def playerAddPoints(player, p):
	player['points'] = player['points']+p

def playerAddItem(player ,item):
	player['items'].append(item)

def playerUseItem(player ,item):
	if item in player['items']:
		player['items'].remove(item)
		return True
	else:
		return False

def simpleTest():
	p = makePlayer("roodkapje")

	incrPoints(p)
	addItem(p ,"CuveeDesTrolls")
	addItem(p ,"MacChouffe")
	addItem(p ,"CuveeDesTrolls")

	print p

	useItem(p ,"CuveeDesTrolls")

	print p

#simpleTest()