# !/usr/bin/python

from scapy.all import *
import ipapi
import os

os.system('clear')
print
print ("\033[1;31m")
print (" ██▓ ██▓███       ▄████ ▓█████  ▒█████                                                      ")
print ("▓██▒▓██░  ██▒    ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒                                                    ")
print ("▒██▒▓██░ ██▓▒   ▒██░▄▄▄░▒███   ▒██░  ██▒                                                    ")
print ("░██░▒██▄█▓▒ ▒   ░▓█  ██▓▒▓█  ▄ ▒██   ██░                                                    ")
print ("░██░▒██▒ ░  ░   ░▒▓███▀▒░▒████▒░ ████▓▒░                                                    ")
print ("░▓  ▒▓▒░ ░  ░    ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░                                                     ")
print ("▒ ░░▒ ░          ░   ░  ░ ░  ░  ░ ▒ ▒░                                                      ")
print ("▒ ░░░          ░ ░   ░    ░   ░ ░ ░ ▒                                                       ")
print ("░                    ░    ░  ░    ░ ░                                                       ")
print ("                                                                                            ")
print ("▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▓█████  ██▀███   ▒█████   █    ██ ▄▄▄█████▓▓█████      ")
print ("▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀      ")
print ("▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒███   ▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░▒███        ")
print ("░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄      ")
print ("  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░░▒████▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓   ▒██▒ ░ ░▒████▒     ")
print ("▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░       ")
print ("░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░     ░     ░ ░  ░         ")
print ("░        ░░   ░   ░   ▒   ░           ░     ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░   ░         ░          ")
print ("░           ░  ░░ ░         ░  ░   ░         ░ ░     ░                 ░  ░                 ")
print ("░                                                                                           ")
print ("                                                                                            ")
print (" by: pr()xy 8l4d3                                                                           ")
print (" ver.: 1.0                                                                                  ")
print (" powered by: https://ipapi.co                                                               ")
print ("\033[0;0m")
print

ipapi.location(ip=None, key=None, field=None)

hostname = input(" Define the hostname or IP to trace and locate: ")
print ("")

for i in range(1, 28):

    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    reply = sr1(pkt, verbose=0)
    if reply is None:
        break


    elif reply.type == 3:

        print
        x = ipapi.location(reply.src, None, 'country')
        y = ipapi.location(reply.src, None, 'city')
        lo1 = ipapi.location(reply.src, None, 'longitude')
        la1 = ipapi.location(reply.src, None, 'latitude')
        print ("Traceroute for destination " "\033[1;31m" + hostname + "\033[0;0m is done! IP:%s" % (reply.src))
        print (" Country:" + ' {0}'.format(x))
        print (" City: " + ' {0}'.format(y))
        print (" Longitude:" + ' {0}'.format(lo1))
        print (" Latitude:" + '{0}'.format(la1))
        print ("*" * 40)
        break

    else:
        d = ipapi.location(reply.src, None, 'country')
        c = ipapi.location(reply.src, None, 'city')
        lo = ipapi.location(reply.src, None, 'longitude')
        la = ipapi.location(reply.src, None, 'latitude')
        print ("%d " % i, reply.src)

        print (" Country:" + ' {0}'.format(d))
        print (" City: " + ' {0}'.format(c))
        print (" Longitude:" + ' {0}'.format(lo))
        print (" Latitude:" + '{0}'.format(la))
        print ("*" * 40)

while True:

    com = input('\n\033[1;31m Do you want to obtain more info for specific IP? Enter \'yes\''
                '\n If you want to quit? Enter \'q\''
                '\n ')
    if com == 'q':
        break

    if com == 'yes':
        print ("")
        hostname2 = input(" Please define the IP to get more info: ")
        a = ipapi.location(hostname2, None, None)
        print ("\033[0;0m*" * 40)
        print (a)
        print ("*" * 40)


    else:
        pass
