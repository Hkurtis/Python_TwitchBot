import string

from tsocket import openSocket, sendMsg
from initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ''

def getUser(line):
	#split on the :
    separate = line.split(":",2)
    #split on the !, grab the username from the lefthand side of the !
    user = separate[1].split("!",1)[0]
    return user
def getMsg(line):
    separate = line.split(":",2)
    msg = separate[2]
    return msg

while True:
    pingMsg = s.recv(2048).decode("UTF-8", errors="ignore")
    pMsg = pingMsg.strip('\n\r')
    data = s.recv(1024)
    if data.find ('PING') !=-1:
        s.send('PONG '+data.split()[1]+'\r\n')
    else:
        readbuffer = readbuffer+data
        temp = string.split(readbuffer, '\n')
        readbuffer = temp.pop()

        for line in temp:
            print(line)
                #if pMsg.find("PING :tmi.twitch.tv\r\n"):
            #this should fix the ping/pong messages
            if "PING" in line and Console(line):
                s.send("PONG tmi.twitch.tv\r\n").encode()
                readbuffer = temp.pop()
                break;
        
            usr = getUser(line)
            msg = getMsg(line)
            print usr+" typed :"+msg
            #Replace text with text you want to search for
            if "Text" in msg:
                #send the message in response to said message
                sendMsg(s, "Send your message here")
