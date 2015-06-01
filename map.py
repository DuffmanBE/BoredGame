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

def makeTile(str):
	return {'tile': True , 'type': str }


WIDTH  = 15
HEIGHT = 10
MAP    = [[makeTile('grass') for x in range(HEIGHT)] for x in range(WIDTH)]

def getTile((x,y)): return MAP[x][y]

def getTiles(p):
	return [
	[ getTile( NW(p) ), getTile( N(p) ), getTile( NE(p) ) ] ,
	[ getTile( W(p) ),  getTile( p ),    getTile( E(p) ) ] ,
	[ getTile( SW(p) ), getTile( S(p) ), getTile( SE(p) ) ]
	]

def isWithinBounds((x,y)):
	global WIDTH
	global HEIGHT
	if (x<0) or (y<0) or (x>WIDTH) or (y>HEIGTH):
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


print getTile((12,9))
