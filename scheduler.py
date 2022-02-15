# Cynthia Marie Rivera Sánchez
# 801-19-5470
# CCOM4017 - 002
# Project 1

from threading import Thread
from threading import Semaphore
from threading import Lock
from time import sleep
import socket

N = 10
mutex = Lock()
empty = Semaphore(N)
full = Semaphore(0)

allMsgs = []

data = dict()

#Organize messages inside a list (Shortest Job First)
def Organize(msg):
    global allMsgs
    index = len(allMsgs) - 1

    if(len(allMsgs) == 0):
        allMsgs.insert(0, msg)


    elif(allMsgs[index][1] > msg[1]):
        if(index != 0 and allMsgs[index - 1][1] < msg[1]):
            allMsgs.insert(index, msg)

        else:
            while(index >= 0 and allMsgs[index][1] > msg[1]):
                    index -= 1

            allMsgs.insert(index + 1, msg)

    else:
        while(index < len(allMsgs) and allMsgs[index][1] <= msg[1]):
            index += 1

        allMsgs.insert(index, msg)

# Defines the producer's job
class Producer(Thread):

    # The constructor assign the internal id to the new thread.
    def __init__ (self, t_number):

        # This variable is used to assign an internal id to the thread.
        self.t_number = t_number
        Thread.__init__(self)

    # Define inside what the thread is to do.
    def run(self):
        global allMsgs

        localIP     = "127.0.0.1"

        localPort   = 20001

        bufferSize  = 1024

        #msgFromServer       = "Hello UDP Client"
        #bytesToSend         = str.encode(msgFromServer)

        # Create a datagram socket
        UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

        # Bind to address and ip
        UDPServerSocket.bind((localIP, localPort))
        print("UDP server up and listening")

        # Listen for incoming datagrams
        for i in range(N):
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            clientMsg = format(message)
            clientIP  = "Client IP Address:{}".format(address)

            # Divides string into two entries [direction, sleep time]
            clientMsg = clientMsg.replace("b","")
            clientMsg = clientMsg.replace("'","")
            msg = clientMsg.split(':')
            int_msg_map = map(int, msg)
            int_msg = list(int_msg_map)

            empty.acquire()
            mutex.acquire()

            # Critical region
            Organize(int_msg)

            mutex.release()
            full.release()

        # Sending a reply to client
        # UDPServerSocket.sendto(bytesToSend, address)


# Defines the consumer's job
class Consumer(Thread):

    # The constructor assign the internal id to the new thread.
    def __init__ (self, t_number):

        # This variable is used to assign an internal id to the thread.
        self.t_number = t_number
        Thread.__init__(self)

    # Define inside what the thread is to do.
    def run(self):
        global allMsgs
        global data

        #Removes messages from list
        for i in range(N):
            full.acquire()
            mutex.acquire()

            # Critical region
            k = allMsgs.pop(0)

            mutex.release()
            empty.release()

            # Keeps record of the time consumed by each device
            if(k[0] not in data):
                data[k[0]] = k[1]

            else:
                value = data.get(k[0])
                data[k[0]] = value + k[1]

            sleep(k[1])

# Python main funtion.  Not necessary but to keep your C++ legacy...
def main():

    # In kernel threads you would like to set this variable
    # to the number of cores in the system.
    idealThreads = 2

    thread = [0] * idealThreads # [0, 0]

    # Create and start the threads
    thread[0] = Producer(0)
    thread[0].start()

    thread[1] = Consumer(1)
    thread[1].start()

    # Make the original thread wait for the created threads.
    for i in range(idealThreads):
        thread[i].join()

    for key in data:
        print("Device " + str(key) + " consumed " + str(data[key]) + " of CPU time.")

if __name__ == "__main__":
    main()
