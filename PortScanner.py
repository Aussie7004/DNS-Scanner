
#DISCLAIMER - Parts of this code was referenced off of https://pythonprogramming.net/python-threaded-port-scanner/ with slight modification for my understanding.
#                                                           For those parts, full credits go to the owners.
#However, majority of this code was written by Aussie7004
import threading
import time
import socket
import sys

from queue import Queue

validIP = False

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
# https://pythonprogramming.net/python-threaded-port-scanner/

print_lock = threading.Lock()
try:
    target = input("Enter WAN or LAN IP or press Ctrl C to exit: ").lower()

    try:
        #This try except will try and resolve the hostname and if it does, it should return ValidIP with true. Otherwise, it prints invalid IP
        DNS = socket.gethostbyname(target)
        validIP = True
            
    except:
        if validIP == False:
            print("Invalid WAN or LAN IP")
            sys.exit()
except KeyboardInterrupt:
    print("You pressed Ctrol C... Quitting")
    sys.exit()



def portScanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        con = s.connect((target, port))
        with print_lock:
            print("Port", port, "Open")
        con.close()

    except:
        pass


def threader():
    while True:

        Init = q.get()

        portScanner(Init)

        q.task_done()


q = Queue()

#how many threads will be allowed
for x in range(1000):

    t = threading.Thread(target=threader)
    #This makes the threads die (stop functioning) when the main code finishes
    t.kill = True
    #Begins the threading
    t.start()
    
    #This is pretty self explainitory - User enters the port range that they want to scan
startingPort = int(input("Enter your starting port: "))
if startingPort < 1 or startingPort > 65534:
    while startingPort < 1 or startingPort > 65534:
        startingPort = int(input("Enter a valid starting port: "))

endPort = int(input("Enter your ending port: "))
if endPort < startingPort or endPort > 65535:
    while endPort < startingPort or endPort > 65535:
        endPort = int(input("Enter a valid ending port: "))
#Time starts to calculate total time later on
start = time.time()

#Scans the specified port range the user entered
for PortScan in range(startingPort, endPort):
    #Puts this for loop in the queue
    q.put(PortScan)

#Q.join() blocks any other processes executing until all the items in the queue are processed and finished. 
q.join()
timeEnd = time.time()

#Calculates time elapsed
totalTime = timeEnd - start
print("\nScan finished in", totalTime, "seconds")
print("\nThank you for using DNS Scanner made by Aussie7004 aka CountTo8\n")
#Weird error idk how to fix - program doesn't end after this and you can't Ctrl C
#Tried doing sys.exit(), exit(), quit() and Ctrl C but nothing works... 
