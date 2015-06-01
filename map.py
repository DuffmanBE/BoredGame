#!/usr/bin/env python

'''
    3 global variables: WIDTH HEIGHT and MAP
    
    y
    ^
    |
    |H
    |E
    |I
    |G
    |H
    |T
    |
    +-WIDTH--------------> x
    
    
'''

# rfid -> (x,y)
TABLE = dict()

def id2coord(id):
	return TABLE[id]

def makeTile(x,y,str, id):
	global TABLE
	TABLE[id] = (x,y)
	return {'tile': True , 'type': str , 'rfid': id}


WIDTH  = 15
HEIGHT = 10
MAP    = [ [makeTile(x,y,"grass", ((1000*x)+y) ) for y in range(HEIGHT)] for x in range(WIDTH)]



def getTileFromId(id):
	return getTileFromCoord( id2coord(id) )

def getTilesFromId(id):
	return getTilesFromCoord( id2coord(id) )

def getTileFromCoord((x,y)):
	if ( isWithinBounds((x,y)) ):
		return MAP[x][y]
	else:
		return False

def getTilesFromCoord(p):
	return [
	[ getTileFromCoord( NW(p) ), getTileFromCoord( N(p) ), getTileFromCoord( NE(p) ) ] ,
	[ getTileFromCoord( W(p) ),  getTileFromCoord( p ),    getTileFromCoord( E(p) ) ] ,
	[ getTileFromCoord( SW(p) ), getTileFromCoord( S(p) ), getTileFromCoord( SE(p) ) ]
	]

def isWithinBounds((x,y)):
	global WIDTH
	global HEIGHT
	if (x<0) or (y<0) or (x>=WIDTH) or (y>=HEIGHT):
		return False
	else: 
		return True

def N((x,y)): return (x   , y+1)
def S((x,y)): return (x   , y-1)
def E((x,y)): return (x-1 , y)
def W((x,y)): return (x+1 , y)

def NE((x,y)): return (x+1  , y+1)
def NW((x,y)): return (x-1  , y+1)
def SE((x,y)): return (x+1  , y-1)
def SW((x,y)): return (x-1  , y-1)

def asPoint(x,y): return (x,y)


print getTilesFromCoord((12,9))
print getTilesFromId(12009)
