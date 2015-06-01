#!/usr/bin/env python

'''
    3 global variables: WIDTH HEIGHT and MAP
    
   
    +-WIDTH--------------> col
    |
    |H
    |E
    |I
    |G
    |H
    |T
    |
    v
    row
    
    
'''

# rfid -> (x,y)
TABLE = dict()

def id2coord(id):
	return TABLE[id]

def makeTile(row,col,str, id):
	global TABLE
	TABLE[id] = (row,col)
	return {
	'tile'      : True ,
	'type'      : str ,
	'rfid'      : id,
	'character' : False , 
	'items'     : list()
}


WIDTH  = 5
HEIGHT = 5
G = "grass"
D = "dirt"
F = "fogg"
HARD_CODED_MAP = [
[F,G,F,F,F],
[F,G,G,G,F],
[F,F,F,G,F],
[F,F,G,G,F],
[F,F,G,F,F],
]

MAP = [ [makeTile(row,col,HARD_CODED_MAP[row][col], ((1000*row)+col) ) for col in range(WIDTH)] for row in range(HEIGHT)]



def getTileFromId(id):
	return getTileFromCoord( id2coord(id) )

def getTilesFromId(id):
	return getTilesFromCoord( id2coord(id) )

def getTileFromCoord((row,col)):
	if ( isWithinBounds((row,col)) ):
		return MAP[row][col]
	else:
		return False

def getTilesFromCoord(p):
	return [
	[ getTileFromCoord( NW(p) ), getTileFromCoord( N(p) ), getTileFromCoord( NE(p) ) ] ,
	[ getTileFromCoord( W(p) ),  getTileFromCoord( p ),    getTileFromCoord( E(p) ) ] ,
	[ getTileFromCoord( SW(p) ), getTileFromCoord( S(p) ), getTileFromCoord( SE(p) ) ]
	]

def isWithinBounds((row,col)):
	global WIDTH
	global HEIGHT
	if (row<0) or (row<0) or (col>=WIDTH) or (row>=HEIGHT):
		return False
	else: 
		return True

def N((row,col)): return (row   , col-1)
def S((row,col)): return (row   , col+1)
def W((row,col)): return (row-1 , col)
def E((row,col)): return (row+1 , col)

def NE((row,col)): return (row+1  , col-1)
def NW((row,col)): return (row-1  , col-1)
def SE((row,col)): return (row+1  , col+1)
def SW((row,col)): return (row-1  , col+1)

def asPoint(row,col): return (row,col)

#
# Set tile content
#
def tileSetCharacter(tile, character):
	tile['character'] = character

def tileUnsetCharacter(tile, character):
	tile['character'] = False

def tileAddItem(tile ,item):
	tile['items'].append(item)

def tileUseItem(tile ,item):
	if tile in player['items']:
		tile['items'].remove(item)
		return True
	else:
		return False


def simpleTest():
	print getTileFromCoord((0,0))
	print getTileFromCoord(S((0,0)))
	print getTileFromCoord(E((0,0)))

simpleTest()