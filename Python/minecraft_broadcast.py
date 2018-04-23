#!/usr/bin/env python3
import socket
import time
import re
import os

import minestat

minecraft_path = "/opt/minecraft"
filename = "server.properties"

servers = []

BROADCAST_IP = "255.255.255.255"
BROADCAST_PORT = 4445

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


#print "Detecting Servers in " + minecraft_path

while 1:
    for path in os.listdir(minecraft_path):  
        target = os.path.join(minecraft_path,path, filename)
        if os.path.isfile(target):    # make sure it's a file, not a directory entry
            with open(target) as f:   # open file
                for line in f:       # process line by line
                    if 'motd' in line:    # search for string
                        #print 'found string %s in file %s' % ( line, target )
                        name = line.split('=')[1].rstrip()
                    if 'server-port' in line:
                        #print 'found string %s in file %s' % ( line, target )
                        port = line.split('=')[1].rstrip()
                servers.append([ name.replace('\\', ''), int(port) ])
            
    #print servers
 #   print "Broadcasting Minecraft servers to LAN"

    for server in servers:

       ms = minestat.MineStat('0.0.0.0', server[1])
       if ms.online:
           msg = "[MOTD]%s[/MOTD][AD]%s[/AD]" % (server[0], server[1])
           #print "advertising " + msg
           #print('Server is online running version %s with %s out of %s players.' % (ms.version, ms.current_players, ms.max_players))
           sock.sendto(msg.encode(), (BROADCAST_IP, BROADCAST_PORT))
       #else:
       #    print( '0.0.0.0:' + str(server[1]) + " is Offline, Skipping")
    time.sleep(5)
