import string
from tsocket import sendMsg

#initialize stuff
def joinRoom(s):
    #print 'joining the room'
    readbuffer =""
    Loading = True
    while Loading:
    	readbuffer = readbuffer+s.recv(1024)
        temp = string.split(readbuffer, '\n')
        #print temp
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    #send msg to the chat
    sendMsg(s,"I'm actually a bot now")

def loadingComplete(line):
    #print 'begining loadingComplete'
    if("End of /NAMES list" in line):
        return False
    else:
        return True