import socket
from settings import HOST, PORT, PASS, ID, CHANNEL

#opens up a connection to twitch.tv and the specific channel you want the bot to be in
def openSocket():
    #print 'opening socket'
    s = socket.socket()
    s.connect((HOST,PORT))
    #sending info to sign in to twitch
    s.send("PASS "+PASS+'\r\n') #pass oauthkeykshdfjkhsd\r\n
    s.send("NICK "+ID+'\r\n')
    s.send("JOIN #"+CHANNEL+'\r\n')
    #print 'sent stuff via the socket'
    return s

def sendMsg(s,message):
    #print 'sending message'
    messageTmp = "PRIVMSG #"+CHANNEL+' :'+message
    s.send(messageTmp+'\r\n')
    print("sent: "+messageTmp)