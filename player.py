#!/usr/bin/env python


def makePlayer(character):
	return {'player' : True , 'character' : character , 'points' : 0 , 'items' : list() }

def decrPoints(player):
	player['points'] = player['points']-1

def incrPoints(player):
	player['points'] = player['points']+1

def addItem(player ,item):
	player['items'].append(item)

def useItem(player ,item):
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