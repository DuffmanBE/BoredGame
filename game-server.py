import json
from map import *
from player import *
from websocket_server import WebsocketServer

characters = dict()
last_position = {'char1': 0, 'char2': 5, 'char3': 7000, 'char4': 7005}

def init_game():
    makePlayer('char1')
    makePlayer('char2')
    makePlayer('char3')
    makePlayer('char4')
    tileSetCharacter(getTileFromId(last_position['char1']),'char1')
    tileSetCharacter(getTileFromId(last_position['char2']),'char2')
    tileSetCharacter(getTileFromId(last_position['char3']),'char3')
    tileSetCharacter(getTileFromId(last_position['char4']),'char4')

# Called for every client connecting (after handshake)
def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])
    #client_ids.append(client)
    characters[client['id']]= makePlayer('char'+str(client['id']))
    tileSetCharacter(getTileFromId(last_position['char1']),'char1')
    server.send_message_to_all("Hey all, a new client has joined us")
    print characters


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message (This happens when player moves)
def message_received(client, server, message):
    #mymsg = "{\"action\": \"claim_char\", \"id\": \"1337\"}"
    jsonobj = json.loads(message)
    print jsonobj
    print client['id']
    if(jsonobj['action'] == "move"):
        print("move action")
        character = characters[client['id']]['character']
        tileUnsetCharacter(getTileFromId(last_position[character]), character)
        tileSetCharacter(getTileFromId(int(jsonobj['id'])), character)
        last_position[character] = int(jsonobj['id'])
        tiles = getTilesFromId(int(jsonobj['id']))
        tilelist = list()
        for row in tiles:
            for tile in row:
                tilelist.append(tile)
        reply = json.dumps(tilelist)
        #print tiles
        #print tiles[0][0]
        #reply = "[{\"tile\": \"True\", \"type\": \"grass\", \"xco\": \"0\", \"yco\": \"0\", \"char\": \"char1\" }]"
        server.send_message(client, reply)
    if(jsonobj['action'] == "claim_char"):
        print("Character selection")
        #characters[client['id']]= makePlayer('char'+str(client['id']))
    print("chars")
    print characters
    print("last_position")
    print last_position

	#print("Client(%d) said: %s" % (client['id'], message))

def send_position(client):

    server.send_message(client)

PORT=9001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
