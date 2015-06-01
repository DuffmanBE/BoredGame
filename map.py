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

WIDTH  = 15
HEIGHT = 10
MAP    = [[False for x in range(HEIGHT)] for x in range(WIDTH)]

def getTile((x,y)): return MAP[x][y]

def isWithinBounds((x,y)):
	global WIDTH
	global HEIGHT
	if (x<0) or (y<0) or (x>WIDTH) or (y>HEIGTH):
		return False
	else: 
		return True

def up((x,y)):    return (x   , y+1)
def down((x,y)):  return (x   , y-1)
def left((x,y)):  return (x-1 , y)
def right((x,y)): return (x+1 , y)

def asPoint(x,y): return (x,y)


print getTile((12,9))
